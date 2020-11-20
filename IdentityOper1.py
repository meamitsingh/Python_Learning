# Program to understand identity and membership operators

list1 = [10,20,30]
list2 = [10,20,30]
print(id(list1))
print(id(list2))
print(list1 is list2) # is tells whether list1 is same as list2==> returns False
print(list1 == list2) # == is content comparison operator tells contents of list1 is same as list2 or not ==> Returns true in this case