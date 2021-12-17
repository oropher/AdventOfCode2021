



with open("D:\\AdventOfCode2021\\01\\input-a.big", 'r') as f:
    tmp = None
    increased = 0
    for line in f.readlines():
        if tmp != None:
            curr = int(line.rstrip('\n'))
            if curr > tmp:
                increased+=1
            tmp = curr
        else:
            tmp = int(line.rstrip('\n'))
    print(increased, ' with ', f.name)
    f.close()


