def swapFileData():
    File =  input("Enter the file name:- ")
    File =  input("Enter the file name:- ")

with open(File1, 'r') as a:
 data_a = a.read()

with open(File2, 'r') as a:
 data_b = b.read()

with open(File1, 'w') as a:
 a.write(data_b)

with open(File2, 'w') as a:
 b.write(data_a)
swapFileData()
