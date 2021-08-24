step=0
def hanoi(n,a,b,c):
    global step
    if n>0:
        hanoi(n-1,a,c,b)
        step=step+1
        print('第{}步：move {} from {} to {}'.format(step,n,a,c))    
        hanoi(n-1,b,a,c)

hanoi(5,'A','B','C')
