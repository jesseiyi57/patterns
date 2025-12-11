rowsize = int(input("enter the num of rows in use"))
if rowsize %2 ==0:
    h = int(rowsize /2)
else:
    h = int(rowsize /2)+1
s = h-1
for i in range (1, h+1):
    for j in range (1, s+1):
        print (" ")
    s = s-1
    num = 1
    for j in range (2*i-1):
        print (end = str (num))
        num = num +1
    print ()
s=1
for i in range(1, h):
    for j in range(1, s+1):
        print (end = " ")
    s = s+1
    num  = 1
    for j in range (1, 2*(h-i)):
        print (end = str(num))
        num = num+1
    print()