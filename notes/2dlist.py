# 2d list is a list of list like a matrix or excel sheet

fruits      =    ["apple", "orange", "banana", "coconut"]
vegetables  =    ["celery", "carrots", "potatoes"       ]
meats       =    ["chicken", "fish", "turkey"           ]

grocieries = [fruits, vegetables, meats]
# [row][column]
print(grocieries[1][0])


# groceries2 == groceries
groceries2 =    [["apple", "orange", "banana", "coconut"],
                 ["celery", "carrots", "potatoes"       ],
                 ["chicken", "fish", "turkey"           ]]

print(groceries2[0][0])
