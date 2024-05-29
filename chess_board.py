board=[]
check1={}
check2={}
my_li=[]
y,x=map(int,input().split())
for i in range(y):
    board.append(str(input()))
    check1[i]=[]
    check2[i]=[]
for test_y in range(0,y):
    if test_y in range(0,y,2):
        for test_x in range(0,x):
            if test_x in range(0,x,2):
                if board[test_y][test_x] == "W":
                    check1[test_y].append(0)
                else:
                    check1[test_y].append(1)
            else:
                if board[test_y][test_x] == "B":
                    check1[test_y].append(0)
                else:
                    check1[test_y].append(1)
    else:
        for test_x in range(0,x):
            if test_x in range(0,x,2):
                if board[test_y][test_x] == "B":
                    check1[test_y].append(0)
                else:
                    check1[test_y].append(1)
            else:
                if board[test_y][test_x] == "W":
                    check1[test_y].append(0)
                else:
                    check1[test_y].append(1)
for test_y in range(0,y):
    if test_y in range(0,y,2):
        for test_x in range(0,x):
            if test_x in range(0,x,2):
                if board[test_y][test_x] == "B":
                    check2[test_y].append(0)
                else:
                    check2[test_y].append(1)
            else:
                if board[test_y][test_x] == "W":
                    check2[test_y].append(0)
                else:
                    check2[test_y].append(1)
    else:
        for test_x in range(0,x):
            if test_x in range(0,x,2):
                if board[test_y][test_x] == "W":
                    check2[test_y].append(0)
                else:
                    check2[test_y].append(1)
            else:
                if board[test_y][test_x] == "B":
                    check2[test_y].append(0)
                else:
                    check2[test_y].append(1)
for a in range(0,x-7):
    for b in range(0,y-7):
        k1=0
        k2=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                k1=k1+check1[j][i]
                k2=k2+check2[j][i]
        my_li.append(k1)
        my_li.append(k2)
print(min(my_li))