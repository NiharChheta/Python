list = [100,True,False,3.14] # mixed type 
print(list)

#does not copy list it create reference (mirror copy) of list 
# list2 = list

#shallow copy (xerox copy)
list2 = list.copy()
print(list2)

#change in list 
list[0] = 10000 

#change in list2 
list2[1] = "Ankit Patel"
print(list)
print(list2)