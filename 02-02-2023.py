#For Loops
#range(start = 0 , end, stepsize= 1)
#for i in range(1,10):
  # print(i)

print("***************")

#while

# i = 1
# while i < 11:
#     print(i)
#     i += 1


# for i in range(10):
#         if i==4:
#             break
#             print(i)

S = "Ahmed"
# for i in S:
#     print(i)
#
#
# for x in range(len(S))
#     print(S[x])

# for i, v in enumerate(S):
#     print(i,v,sep='.')

print("***************")
# input = 5
# sum = 0
# for i in range(1, input+1):
#    sum += i
#    print(sum)

input = 'mohamed'
vowels = 'aeoiu'
charcount = 0
for x in input:
   if x in vowels:
      charcount +=1

print (charcount)


# Given a string, write a python program that convert the string based on the following conditions:
# • If lower case letter less than upper case letter convert string to upper case
# • If upper case letter less than lower case letter convert string to upper case

input ="AhMEd"
lowercaseCount=0
uppercasCount=0
for i in input:
    if i.isupper():
        uppercasCount +=1
    else:
        lowercaseCount += 1

if lowercaseCount < uppercasCount:
   print(input.upper())

else:
   print(input.lower())



