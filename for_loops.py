# for loops = execute a block of code a fixed number of times.
#             You can iterave over a range, string, sequence, etc...
#             range( [start : end : step] )

# the 1st value is inclussive the 2nd is exlussive 
# so the for loop goes through values 1 to 10
for x in range(1,11):
    print(x)

print("\nreversed values:")

for x in reversed(range(1,11)):
    print(x)


# how to skip the unlucky number 13
print("\nhow to skip the unlucky number 13")
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)