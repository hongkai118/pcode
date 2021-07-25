#-*-coding:utf-8-*-
#功能介绍：运行时将指数的点数，直接放入文件中
import requests
import xlwings as xw
wb = xw.Book("zhishu.xlsx")
sht = wb.sheets["sheet1"]


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}
#指数列表
session= requests.Session()

# all_url = 'https://stock.xueqiu.com/v5/stock/batch/quote.json?symbol=SH000300,SH000905,SZ399006,SH000001,SH000016,SH000170,SZ399550,SZ399001,SH000015,SH000922,SZ399324,SZ399925,SZ399701,SH000803,SH000804,SZ399812,SH000932,SH000933,SH000978,SZ399989,SZ399986,SZ399975,CSI930651,CSI931087,CSI931461,CSI931406,CSIH11136,CSIH30184&extend=detail'
all_url='https://stock.xueqiu.com/v5/stock/batch/quote.json?symbol=SH000300,SH000905,SZ399006,SH000001,SH000016,SH000170,SZ399550,SZ399001,SH000015,SH000922,SZ399324,SZ399925,SZ399701,SH000803,SH000804,SH000919,SZ399812,SH000932,SH000933,SH000978,SZ399989,SZ399986,SZ399975,CSI931087,CSI930651,CSI931461,CSI931406,CSIH11136,CSIH30184&extend=detail&is_delay_hk=true'
def get_stock_info(zhishu_url,start_l='A',start_h=1):
    try:
        session.get('https://xueqiu.com/',headers=headers,timeout =5)

        r = session.get(url=zhishu_url, headers=headers)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        pp= r.json()
        zs_numbers = len(pp['data']['items']) #获取总共多少支指数
        print('获取股票指数数量：',zs_numbers)
    except:
        print("获取网页失败")

#迭代
    for i in range(zs_numbers):
        zhishu_name = pp['data']['items'][i]['quote']['name'] #指数名称
        zhishu_code = pp['data']['items'][i]['quote']['symbol'] #指数代码
        zhishu_info = pp['data']['items'][i]['quote']['current'] #当前点数

        #再单元格中写入批量数据，只需要指定其单元格位置
        sst = start_l+str(start_h+i)
        print(i+1,zhishu_name,zhishu_code,zhishu_info)
        sht.range(sst).value = [zhishu_info]

if __name__ =='__main__':
    get_stock_info(all_url,'h',2) #获取URL,列，行；默认从A1开始
