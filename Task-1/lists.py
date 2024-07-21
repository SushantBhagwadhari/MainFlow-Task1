# Lists are like dynamically sized Arrays, and are not always homogeneous. A single list may contain Integers, Strings and objects.
# Lists are mutable, and hence, they can be altered even after their creation. Lists in Python are ordered and have a definite count.

# Example of a mixed type list:
myList = [1, 69, "Alisa", 420, "Rias", 7]
print("\n List with the use of Mixed Values: ")
print(myList)

# Appending the python:
# This means that we can add extra elements, Tuples, or even another list to a list in python.

# Example:

myList.append(169)
myList.append("Tohka")
print(myList)
myList.append((269, 69420))
print(myList)
myList2 = [2, 3, 4, "Akeno", "Mikoto"]
myList.append(myList2)
print(myList)

