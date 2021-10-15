

def matriz():
    l = []
    a = int(input())
    b = int(input())
    if a > 0 and b > 0: 
        for i in range(a):
            l.append([])
            for j in range(b):
                num = int(input())
                l[i].append(num)
    else: 
        print('Error')
    return l

def main():
    m = matriz()
    l_c = []
    if len(m) > 0:
        for i in range(len(m[0])):
            n = 0
            for k in range(len(m)):
                n += m[k][i] 
            l_c.append(n)
        print(l_c)



if __name__=='__main__':
    main()
