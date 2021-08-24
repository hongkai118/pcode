# 解法1  逐字检查
def anagramSolution1(s1, s2):
    # 1)将s2变成list
    # 2)从s1中取第1个字符，与s2中逐个进行比较，有就打勾（下次不检查），没有就返回False
    # 3)按照第2步，从s1中取2个与s2逐字比较，一直到s1中所有字符串比较完
    # 性能分析，外层循环执行n次，内层循环执行，1，2，3，。。。n-1次==》所有复杂度，是 n(n+1）/2=O(n**2)

    alist = list(s2)
    pos1 = 0
    result = True  # 展示结果

    # 取s1的字符
    while pos1 < len(s1) and result:

        # 逐个与s2进行比较
        pos2 = 0
        found = False

        while pos2 < len(s2) and not found:

            if s1[pos1] == alist[pos2]:
                found = True
                alist[pos2] = None
            else:
                pos2 = pos2 + 1

        if found:
            pos1 = pos1 + 1
        else:
            result = False

    return result


def anagramSolution2(s1, s2):
    #先转换成列表，逐个对比。
    #复杂度：排序的复杂度是 n**2或者n Log(N)
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    result = True
    while pos < len(s2) and result:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            result = False

    return result

# # 3暴力法 写不来；n!
# def anagramSolution3(s1,s2):
#     #1)将S1的全排列弄出来
#     alist1=list(s1)
#     if len(alist1) <

# 计数比较-程序代码
# 性能 T(n)= 2n + 26===> O(n)
def anagramSolution4(s1,s2):
    #1 将26个字母做成26个各自，统计每个字母出现的次数
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos]+1

    #比较两个出现的次数
    result = True
    j = 0
    while j < 26 and result:
        if c1[j]==c2[j]:
            j=j+1
        else:
            result=False
    return result




if __name__ == '__main__':
    result=anagramSolution4('aabcdd', 'daabcda')
    print(result)
