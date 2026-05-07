dict={
    "name" : "krish",
    "age" : 21,
    "mark" : 94.0,
    "hobbies" : ["cricket","dance","reading"],

}
dict["age"] = 20 # update
dict["rollno"] = 19 # add new item
print(dict["hobbies"][1])
print(dict)
print(type(dict))

# dictionary method

print(dict.get("name"))

print(dict.keys())

print(dict.values())

print(dict.items())

print(len(dict.items()))

dict.update({"name" : "krishhirani"})
print(dict)

dict.pop("age")
print(dict)

dict.clear()
print(dict)



# set
s={1,2,2,3,4,1,4,5} # Duplicate Values Not Allowed
es=set() # empty set
print(es)

print(s) #Duplicate Values Not Allowed
print(type(s))

# set method
s.add(7)
print(s)

s.remove(2) # remove the Specific element
print(s)

s.pop() # remove randam value
print(s)

s.clear()
print(s)