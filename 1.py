print("hello world")
import random

def getThreeNumbers():
    myList=[]
    nums=''
    while True:
        num=random.randint(1,10)
        if num not in myList:
            myList.append(num)
            nums=nums+str(num)
        if len(myList) == 3:
            break
    return nums

def getThreeNumbersFromLUser():
        while True:
            print('Input 3-digit numbers')
            num=str(input())
            numList = list(num)
            if len(numList)>3:
                print(num,' is an invalid input. Try again.')
            elif (int(numList[0]) in range(0,10) and int(numList[1]) in range(0,10) and int(numList[2]) in range(0,10)) == False:
                print(num,' is an invalid input. Try again.')
            elif 0<=int(num)<1000 == False:
                print(num,' is an invalid input. Try again.')
            elif numList[0] == numList[1] or numList[0] == numList[2] or numList[1] == numList[2]:
                print(num,' is an invalid input. Try again.')
            else:
                break
        return num

def checkNumbers(inputNumbers):
    global nums
    strikeBallOut=[]
    myList=list(str(nums))
    strike=0
    ball=0
    out=0
    numList=list(str(inputNumbers))
    for x in range(0,3):
        if numList[x] == myList[x]:
            strike=strike+1
        elif numList[x] in myList:
            ball=ball+1
        else:
            out=out+1
    strikeBallOut.append(strike)
    strikeBallOut.append(ball)
    strikeBallOut.append(out)
    return strikeBallOut

nums = getThreeNumbers()
print('Baseball game starts!')
for x in range(0,5):
    numsFromUser=getThreeNumbersFromLUser()
    myList=checkNumbers(numsFromUser)
    if myList[0] == 3:
        print(numsFromUser,': 3S')
        print('You Win!')
        break
    if myList[2] == 3:
        print('Out!')
    else:
        print(f'{numsFromUser}: {myList[0]}S {myList[1]}B {myList[2]}O')
    if x == 4:
        print('You Lose! The number is ',nums)
    
    


