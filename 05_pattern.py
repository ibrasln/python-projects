'''
Print the following pattern.
1
22
333
....
nnn..
'''

rows = int(input("Enter row size:"))
num = 0
for i in range(rows + 1):
    for j in range(i):
        print(num, end = '')
    
    num += 1
    print("")
    