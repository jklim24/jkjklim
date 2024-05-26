dic={}
n=int(input())
for i in range(0,n):
    a,b=map(str,input().split())
    a=int(a)
    if a in dic.keys():
        dic[a].append(b)
    else:
        dic[a]=[b]
li=list(dic.keys())
li.sort()
for x in li:
    for y in dic[x]:
        print(str(x)+" "+str(y))