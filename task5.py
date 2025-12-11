"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

def findstock(file):
    dsymbol = {}
    data = file.read()
    lines = data.split('\n')
    slines = []
    for i in lines:
        n = i.split(',')
        slines.append(n)
    for i in slines:
        dsymbol[i[0]] = i[1]
    find = input("Enter the symbol of a stock to search for it's name: ")
    matches =[]
    while len(matches) != 1:
        for i in dsymbol: 
            if find in i:
                matches.append(i)
        if len(matches) == 1:
            print(dsymbol[matches[0]])
        elif len(matches) > 1:
            print(f'There are {len(matches)} stocks with that symbol')
            find = input(f'Please enter a symbol on this list: {matches}: ')
        else:
            print("No matches found")
            find = input("Enter the symbol of a stock to search for it's name: ")


##Need top debug a bit more
        








file = open('task5.csv', 'r')

findstock(file)