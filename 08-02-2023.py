'''
1- 2 D List
2- Dictionaries
3- OOP
4- Github

//*****************************
import numpy as np
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)
'''

"""
class_list = [
["Mohamed", 18, 3.00],
["Yara", 19, 4.00],
["Omar", 18, 3.75]
]

print(class_list)
#col row
print(class_list[0][0])
print(class_list[1][1])

class_list.append(["Mohsen", 20, 2.5])

class_list.sort()

print(class_list)

print(class_list[0])

print(class_list[2][2])

for i in class_list: # rows
    for j in i: # cols
        print(j)
"""


#======================================

"""
dic = {
    "key": value(int, list, string, dect)
}


dic = {
    "student_1":[12,13,14],
    "student_2":"Mohamed",
    "student_3":{"course_1":89, "course_2":70},
    "student_4":""
}

print(dic)
print(dic['student_3']['course_2'])
#dic.pop("student_3")
dic['new']=999
print(dic)
print(dic.keys())
print(dic.values())
"""
#==========================
"""
dict_data = {

"brand": "Ford",
"model": "Mustang",
"year": 1964
}

dict_data["color"] = "red"
print(dict_data)
dict_data.pop('brand')
#print(dict_data['brand'])
dict_data['year']= 2023
print(dict_data)
dict_data ={
"brand" : "BMW",
"model" : "320i",
"year" : "2020",
"color" : "black"
}
print(dict_data)

dict_data.clear()
print(dict_data)
"""
#=================================
class Human:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        print("Welcome To {} age {} ".format(name,age))


x = Human("kareem", 39)
print()



class BankAccount:
    def __init__(self,accountNumber,balance,interestRate=0.05):
        self.accountNumber = accountNumber
        self.balance = balance
        self.interestRate = interestRate


client = BankAccount("oo767667",25000)
print(client.interestRate)







