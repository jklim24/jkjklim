t=int(input())
for x in range(0,t):
    n,word=map(str,input().split())
    n=int(n)
    for a in range(0,len(word)):
        for b in range(0,n):
            print(word[a],end='')
    print()