
md5 解密方法：（MD5加密为16进制的32位数据）
    from hashlib import md5
    result='adafadfaafadfadfafadfadf'
    md=md5()
    #将字符串打包到md5中
    md.update(result.encode())
    #解码
    decode_result = md.hexdigest()

base 64 解密方法：
    import base64
    result = 'xxxxxxx,adfadfadfdfdafd'
    b=base64.b64decode(result) #输出二进制文件,前面又woff字样-->代表woff文件


TTfont 使用方法：
    from fontTools.ttLib import TTFont
    from io import BytesIO
    
    #将二进制数据'b'，存为woff文件。
    with open('ztku.woff','wb') as f:
        f.write(b)
        
    #用TTFont打开woff文件
    fonts = TTFont('ztku.woff')
    #将"ztku.woff'另存为xml文件
    fonts.saveXML('ztku.xml')