#07/17/2014
print ("To screen")

with open('mytestfile.txt', 'w') as f:
    f.write("line one to file\n")
    f.write('line two to file\n')
    
print "File 'mytestfile.txt' is ready for viewing!"

#reading data from file
with open("readme.txt") as f:
    data = f.read()
    print data
    
#while loops
number = 1
while 