# dictionary is an unordered set of key and value pair. It is a container which contains data, enclosed within curly braces.
# dictionary is mutable, but the key must be unique and immutable. Value is accessed by the key. Value can be updated while key cannot be changed.

#Accessing Dictionary Values Example:
dict1 = {1: 'Python', 2: 'Java', 3: 'JavaScript'}
print(dict1[2], dict1[1])

#Updating Dictionary Elements Example:
dict2 = {1: 'Python', 2: 'Java', 3: 'JavaScript'}
dict2[2] = "Unity"
dict2[4] = "Blender"
print(dict2)

#Deleting Dictionary Elements Example:
del dict1[2]
print(dict1)
dict2.clear
print("Dict2: ", dict2)
del dict1
print("Dict1 deleted")

