print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

print的5个参数：
    ——object,暂时看不懂，先不管
    ——sep：输入字符串，默认为空
    ——end: 以什么结尾，默认'\n'为换行。如果想不换行，可以使用空串'',同时flush =True,如果flush=False则会等到下一个print(‘xxxx’)才打印出来。
    ——file: 太了解，先不管。
    ——flush: 见第三个参数end的配套使用；flush=True,简单说就是将缓存里面的内容立即输出到标准输出流(这里是sys.stdout, 也就是默认的显示器)