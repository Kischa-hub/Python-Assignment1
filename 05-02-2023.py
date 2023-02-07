# 1 Functions
# 2  Lists - Tuples - dict - sets


"""
def calculateSum(x,y=0):
   print (x+y)

print(calculateSum(3,7))


have used Python Tutor to visualize over 200 million pieces of code. 
It is the most widely-used program visualization tool for computing education.


x = "Kohamed"
x = list (x)
x[0]= 'M'
print ('*'.join(x))

xx = [1,2,3,4]
xx.append(99)
xx.insert(0,"Hallo")
xx.append([44,32,90])
xx.extend([44,32,90])

del xx[0]
xx.pop()
xx.remove(99)
#xx.reverse()

print(xx)
"""
"""
=====================================




#tuple in immutable
#t = ("Ahmed",1,2,3,4)
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
evnumbers = L[1::2]
oddnumbers = L[::2]
print(evnumbers)
print(oddnumbers)
L2 = evnumbers + oddnumbers
print (L2)
del L2[::2]
print (L2)
L2.append(10)
print (L2)
L2.sort()
print (L2)
=====================================
"""
#Tuples
t =(2,"text",3) +(4,5)
#print(t)
#print(t[2])
#t[1]=4
#print(t[::2])

x = "x3"
y = "y3"

temp = x
x = y
y = temp

name = "Kareem"
L=[1,2,3,4,5]
L[1]=10
L.append(40)
L.extend([0,7])
L.remove(0)
L.pop()
del(L[1])
total = 0
for i in range(len(L)) :
    total +=L[i]

print(total)
print(L)
test = name.split()
print(test)


L=[9,6,0,3]
L.sort()
L.reverse()

print(0 in L)

#======================



