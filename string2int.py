import re
input = input()
# compare an input to the regular expression format of decimal
integers = ["0","1","2","3","4","5","6","7","8","9"]
output = 0
for i in input:
    for j in integers:
        if i == j :
            output = ((output * 10) + integers.index(j)) 

print(output)

