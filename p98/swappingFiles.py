def swapFileData():
    filename1 = input("Enter the name of the first file:")
    filename2 = input("Enter the name of the second file:")

    a = open(filename1, 'r')
    data_a = a.read()
    a.close()

    b = open(filename2, 'r')
    data_b = b.read()
    b.close()

    a = open(filename1, 'w')
    a.write(data_b)
    a.close()

    b = open(filename2, 'w')
    b.write(data_a)
    b.close()
    

swapFileData()