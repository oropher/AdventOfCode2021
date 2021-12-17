



with open("D:\\AdventOfCode2021\\01\\input-a.small", 'r') as f:
    first = None
    second = None
    temp = None
    increased = 0
    for line in f.readlines():
        if first != None:
            if second != None:
                curr = int(line.rstrip('\n'))
                if tmp != None:
                    
                else:
                    tmp = first + second + curr
                first = second
                second = curr
            
            else:
                second = int(line.rstrip('\n'))
        else:
            first = int(line.rstrip('\n'))
    print(increased, ' with ', f.name)
    f.close()
    




