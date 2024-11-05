with open("test.txt") as f:
    #print(f.read())
    # print(f.readline())
    # line=f.readline()
    # while line!="":
    #     print(line)
    #     line=f.readline()
    for line in f.readlines():
        print(line)

with open("test.txt") as f:
    content=f.readlines()
    reversed(content)
    with open("test.txt",'w') as f:
        for line in reversed(content):
            f.write(line)