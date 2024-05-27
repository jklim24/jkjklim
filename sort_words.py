dic={}
n=int(input())
for i in range(0,50):
    dic[i]=[]
for i in range(0,n):
    my_str=str(input())
    if my_str in dic[len(my_str)]:
        continue
    else:
        dic[len(my_str)].append(my_str)
for i in range(0,50):
    if not dic[i]:
        continue
    else:
        dic[i].sort()
        for word in dic[i]:
            print(word)