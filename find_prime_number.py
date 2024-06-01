def check(num):
    for i in range(3,num,2):
        if num % i == 0:
            return 0
    return 1
t=int(input())
li=list(map(int,input().split()))
ch=0
a=0
max=max(li)
for x in range(0,t):
    a=li[x]
    if a in range(3,max+1,2):
        if check(a) == 1:
            ch=ch+1
    elif a == 2:
        ch=ch+1
print(ch)
