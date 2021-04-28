import re
input = input()
out = re.findall(r"\d+", input)
# compare an input to the regular expression format of decimal
for i in out:
    print(i, end="")