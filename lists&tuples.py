values = [1, 2, "kacper", 4, 5] #list

print(values[0]) #prints first position on the list

print(values[3]) #prints 4th postion on the list

print(values[-1]) #prints last postion on the list

print(values[1:4]) #prints postions from 2nd to 4th

values.insert(3, "biegajło") #inserting into list

print(values)

values.append("end") #adding value at end of the list
print(values) 

values[2] = "Kacper" #changing value 

del values[0] #deleting first value in the list

print(values)

values = [1, 2, "kacper", 4, 5] #list

values = (1, 2, "kacper", 4, 5) #tuple so cant be modified unless written over

dic = {"a":2, 4:"bcd", "c":"Hello world"} #dictionary

print(dic[4])
print(dic["c"])

#making dictionary from empty one

dict = {}
dict["firstname"] = "Kacper" 
dict["lastname"] = "Biegajło"
dict["gender"] = "male"
print(dict)
print(dict["lastname"])
