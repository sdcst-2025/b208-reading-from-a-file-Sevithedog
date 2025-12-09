"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
def npytriples(file):
    data = file.read()
    line = data.split("\n")
    while '' in line:
        line.remove('')
    npy = 0
    for i in range(0,len(line),3):
        if (float(line[i]))**2 + (float(line[i +1]))**2 == (float(line[i+2]))**2 or (float(line[i+1]))**2 + (float(line[i+2]))**2 == (float(line[i]))**2 or (float(line[i+2]))**2 + (float(line[i]))**2 == (float(line[i+1]))**2 and float(line[i]) == int(line[i]) and float(line[i+1]) == int(line[i+1]) and float(line[i+2]) == int(line[i+2]):
            npy+=1 
    return npy

a = open('task02a.txt', 'r')
b = open('task02b.txt', 'r')
c = open('task02c.txt', 'r')
assert npytriples(a) == 6
assert npytriples(b) == 4
assert npytriples(c) == 11