import re

regex = re.compile(r"[a-z]+-[a-z]+-[a-z]+|[a-z]+-[a-z]+[ ][a-z]+|[a-z]+-[a-z]+|[a-z]+[ ][a-z]+-[a-z]+|[a-z]+[ ][a-z]+[ ][a-z]+|[a-z]+[ ][a-z]+|[a-z]+")

with open("list_attr_cloth.txt", "r") as f:
    lines=f.readlines()

    with open("list_attr_cloth-parse.txt", "w") as f:
        for x in lines:
            f.write(' '.join(map(str, regex.findall(x)))+', ')
            # f.write(' '.join(map(str, regex.findall(x)))+' ')
            # f.write("'"+' '.join(map(str, regex.findall(x)))+"', ")
            # f.write(str(regex.findall(x)))
