

import os
import fitz
from pyzbar.pyzbar import decode
from PIL import Image
import xlwings as xw


def get_filepath(base_path):
    '''获取当前路径下所有的电子发票pdf文件路径'''
    file_paths = []
    file_names = os.listdir(base_path)
    for file_name in file_names:
        if file_name.endswith('.pdf'):
            file_paths.append(os.path.join(base_path, file_name))
    return file_paths

def rename_pdf(file_paths,yuefen,money):
    '''逐一对所有电子发票文件左上角的二维码识别并重命名文件,
    返回发票日期和金额，便于录入到excel'''
    fapiao_list=[]
    for file_path in file_paths:
        result = get_qrcode(file_path)
        results = list(result.split(','))
        kp_date = results[5][0:4]+'年'+results[5][4:6]+'月'+results[5][6:8]+'日'
        if money == 'y' or money=='':
            new_name = results[4]+'+'+kp_date+'+'+results[2] + "+" + results[3] + '+'+ yuefen+'月'+".pdf"
        else:
            new_name = kp_date+'+'+results[2] + "+" + results[3] + '+'+ yuefen+'月'+".pdf"
        print(new_name)
        new_file_path = os.path.dirname(file_path) + '\\' + new_name       
        os.rename(file_path, new_file_path)
        zuhe= [results[5],results[4]]
        fapiao_list.append(zuhe)
    return fapiao_list
    

def get_qrcode(file_path):
    '''提取pdf文件中左上角的二维码并识别'''
    pdfDoc = fitz.open(file_path)
    page = pdfDoc[0]    #只对第一页的二维码进行识别
    rotate = int(0)
    zoom_x = 3.0
    zoom_y = 3.0
    mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    rect = page.rect

    mp = rect.tl + (rect.br - rect.tl) * 1 / 5

    clip = fitz.Rect(rect.tl, mp)
    pix = page.getPixmap(matrix=mat, alpha=False, clip=clip) #应该是获得二维码坐标
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)  #读取二维码图片
    barcodes = decode(img) #解析二维码图片
    for barcode in barcodes:
        result = barcode.data.decode("utf-8")
        # print(result) #返回 01,10,012002000511（代码）,47490262（号码）,233.02（金额）,20210521（日期）,74154568030742119765（校验码）,83C3,
        return result


if __name__ == '__main__':
    base_path = os.getcwd()
    all_files = get_filepath(base_path)
    yuefen= input('几月（数字）:',) #输入月份
    money=input('是否显示金额（y显示，n不显示）:',)
    excel_y = input('金额录入excel(y录入，n不录):',)

    fapiao_list=rename_pdf(all_files,yuefen=yuefen,money=money)

    if excel_y=='y':
        #打开excel.
        wb=xw.Book()
        sht=wb.sheets['sheet1']
        biaotou = ['日期','金额']
        sht.range('a1').value = biaotou
        sht.range('a2').value=fapiao_list
    
    print('')
    print('本次更改文件名数量：',len(all_files))

    print('xxxxxxxxxxxxxxxxxxxxxxx')
    print('第三版：这里是第三版的更改，在第二版时不会显示')
    print('44444444444444444')

#这一行是在hot_fix分支上进行的操作。

#参考：https://blog.csdn.net/qq_35448080/article/details/114762390
#这一行测试冲突（master)
