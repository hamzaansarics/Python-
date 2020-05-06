with open("E:\simple.txt",'r') as file1:
    with open("E:\simple1.txt",'w') as file2:
        file2.write(file1.read())
