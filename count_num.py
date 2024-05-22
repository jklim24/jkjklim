from collections import Counter
n1=int(input())
li1=list(map(int,input().split()))
n2=int(input())
li2=list(map(int,input().split()))
count_li1=Counter(li1)
for x in li2:
    count_li1.setdefault(x,0)
    print(str(count_li1[x])+" ",end='')