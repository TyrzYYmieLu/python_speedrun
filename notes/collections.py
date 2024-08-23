# collection = single "variable" used to store multiple values
#   List    =  [] ordered and changeable. Dubplicates OK
#   Set     =  {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple   =  () ordered and unchangeable. Duplicates OK. FASTER than list


fruits = {"apple", "orange", "banana", "coconut"}

# List
'''
fruits.append("lego")
print(fruits[:3]) # is the same as fruits[0:3]
print(fruits[::-1])
print("apple" in fruits)

fruits.remove("lego")
print(fruits[::-1])
fruits.insert(0,"elo")
print(fruits[::-1])

# fruits.sort()
# fruits.reverse()
# fruits.claer()
# fruits.count()

print(fruits.index("apple"))
'''
# Set

print(fruits)
print(dir(fruits))

print(fruits[0]) # 'set' object is not subrscriptable
fruits.add()
fruits.remove()
fruits.pop() # this will be random
fruits.clear()