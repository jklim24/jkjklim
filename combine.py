def pec(i):
    if i == 0:
        return 1
    else:
        return pec(i-1)*i
t=int(input())
for i in range(0,t):
    k,n=map(int,input().split())
    print(int(pec(n)//pec(k)//pec(n-k)))