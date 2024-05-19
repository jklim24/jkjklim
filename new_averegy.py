n=int(input())
li=list(map(int,input().split()))
max=max(li)
for x in range(n):
    li[x]=li[x]/max*100
print(sum(li)/n)
