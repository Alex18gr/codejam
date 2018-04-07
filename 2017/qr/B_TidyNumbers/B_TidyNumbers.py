from __future__ import print_function



def inputData():
    infile = open("B-small-practice.in","r")
    #infile = open("temp", "r")
    lines = infile.readlines()
    infile.close()
    return lines

def isTidy(num):
    for i in range(0, len(num) - 1):
        if(num[i] > num[i + 1]):
            return False
    return True

def tidyA(digits):

    #if(digits[0] == '0' and digits[1] == '0'):
        #digits[0] = 9
        #digits[1] = 9
    if(int(digits[0]) > int(digits[1])):
        digits[0] = str(int(digits[0]) - 1)
        digits[1] = 9

    return digits

def tidyB(digits):

    for i in range(0, len(digits)):
        if(int(digits[i]) == 9):
            for j in range(i + 1, len(digits)):
                digits[j] = '9'
            break


    if(int(digits[0]) > int(digits[1])):
        digits[1] = '9'
    return digits

inData = inputData()
inData = [int(x) for x in inData]
n = inData[0]
data = inData[1::]

TidyNumsList = []

for numberInt in data:
    numberStr = str(numberInt)
    nlist = [j for j in numberStr]


    l = len(numberStr) - 1
    numberStr[l] #teleftaio psifeio tou arithmou
    numberStr[0] #to prwto stoixeio tou arithmou


    for i in range (l, 0, -1):
        #print i
        nlist[i - 1], nlist[i] = tidyA([nlist[i-1], nlist[i]])
        #if(isTidy(nlist)):
            #break

    if(not isTidy(nlist)):
        tidyB(nlist)


    tidyStr =  "".join(str(x) for x in nlist)
    tidyInt = int(tidyStr)
    TidyNumsList.append(tidyInt)

print (TidyNumsList)

f = open("output.out", "w")
for i in range(0, len(TidyNumsList)):

    print("Case #",i+1,": ",TidyNumsList[i],sep="" ,file=f)