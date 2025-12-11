#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
def lsum(file):
    lines = file.read()
    print(lines)
    line = lines.split('\n')
    print(line)
    clusters = []
    templist = []
    for i in line:
        if i != '' :
            templist.append(i)
        else:
            clusters.append(templist)
            templist = []
    print(clusters)
    counter = 0 
    for i in clusters:
        n = [float(x) for x in i]
        if sum(n) > counter:
            counter = sum(n)
    print(counter)
    return
            


file = open('task03.txt', 'r')

""" for i in listoflists:
        if sum(i) > counter
        counter = sum(i)

"""
lsum(file)
    
