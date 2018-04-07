from __future__ import print_function

def inputData():
    infile = open("input.data","r")
    #infile = open("temp", "r")
    lines = infile.readlines()
    infile.close()
    return lines

def getFirstMistake(alist):

    for i in range(0, len(alist) - 1):
        if (alist[i] > alist[i+1]):
            return i
    return -1


def bubbleSort(alist):
    lastNotMoved = len(alist)
    finish = False

    for passnum in range(len(alist)-2,0,-1):
        if(finish): break;
        prevLastNotMoved = 0
        prevMoved = False
        for i in range(passnum):
            if alist[i]>alist[i+2]:
                temp = alist[i]
                alist[i] = alist[i+2]
                alist[i+2] = temp

                prevMoved = True
                lastNotMoved = 0
            else:
                if(prevMoved):
                    prevMoved = False
                else:
                    if lastNotMoved == prevLastNotMoved:
                        finish = True
                        break;
                    lastNotMoved += 1
    return getFirstMistake(alist)

def printResult(r):
    if(r == -1):
        return "OK"
    else:
        return r


def __main__():
    #infile = open("input.data", "r") for file reading
    #n = int(infile.readline()) for file reading
    n = int(input())
    f = open("output.out", "w")
    for i in range(0, n):
        #l = int(infile.readline()) for file reading
        l = int(input())
        #print(l)
        #nums = [int(x) for x in infile.readline().split()] #for file reading
        nums = [int(x) for x in input().split()]
        #print(nums)
        result = bubbleSort(nums)
        #print("First Mistake", result)
        #print(nums)
        print("Case #{}: {}".format(i+1, printResult(result)))
        print("Case #", i + 1, ": ", printResult(result) , sep="", file=f)
    #print(n)


if __name__ == '__main__':
    __main__()