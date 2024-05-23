n, k = map(int, input().split())
li = list(range(1, n + 1))
removed_li = []
index = 0
while len(li)>0:
    index = (index + k - 1) % len(li)
    removed_li.append(li.pop(index))
result_str = str(removed_li)
print('<' + result_str.strip("[""]") + '>')