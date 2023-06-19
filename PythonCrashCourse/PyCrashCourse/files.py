# Python has functions for creating, reading, updating, and deleting files

# Open a file
myFile = open("myFile.txt", 'w')  # w = mode ( means writing )

# get info
print('Name:', myFile.name)
print('Is Closed :', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

#Append to file
myFile = open('myFile.txt', 'a') # a = append mode
myFile.write(' I like SUGAGGAGAGAGGAGGAGGR')
# Read from file
myFile = open('myFile.txt', 'r')# r = read
text = myFile.read(100)
print(text)