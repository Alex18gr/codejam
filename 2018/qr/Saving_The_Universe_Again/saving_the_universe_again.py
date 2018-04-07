
def swap_S_with_nearest_C(index, program):
    #for i in range(0, len(program)):
    for i in range(index, -1, -1):
        if(program[i] == 'C'):
            program[i] = 'S'
            program[i+1] = 'C'
            break

def countTotalDmg(program):
    power = 1
    dmg = 0
    for action in program:
        if action == 'C':
            power = power * 2
        else:
            dmg += power
    return dmg

def countSandC(program):
    s, c =[0, 0]
    for action in program:
        if action == 'S':
            s += 1
        else:
            c += 1
    return [s, c]

def hackAlien(d, program):

    s, c = countSandC(program)
    #print(countSandC(program))
    if d < s:
        #print("IMPOSSIBLE")
        return -1
    hacks = 0
    Cs_at_end = 0
    i = len(program) - 1

    while(Cs_at_end < c):

    #for i in range(len(program)-1, c-1, -1):
        if countTotalDmg(program) <= d:
            break
        #print(program[i],end="")
        if program[i] == 'S':
            swap_S_with_nearest_C(i, program)
            hacks += 1
        else:
            Cs_at_end += 1
            i -= 1
    #print(program, hacks)
    return hacks



def __main__():
    #infile = open("data.in", "r") for file reading
    n = int(input())
    #n = int(infile.readline()) for file reading

    for i in range(0, n):
        maxDmg_str, program = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
        #maxDmg_str, program = [x for x in infile.readline().split()]
        maxDmg = int(maxDmg_str)
        program_list = [j for j in program]
        result = hackAlien(maxDmg, program_list)
        if result == -1:
            print("Case #{}: {}".format(i + 1, "IMPOSSIBLE"))
        else:
            print("Case #{}: {}".format(i + 1, result))



if __name__ == '__main__':
    __main__()