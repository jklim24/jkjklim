def pec(i):
    if i == 0:
        return 1
    else:
        return pec(i-1)*i
n,k=map(int,input().split())
print(int(pec(n)/pec(k)/pec(n-k)))
