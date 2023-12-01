inputs = []

f = open("input.txt", "r")
for i in f.readlines():
    inputs.append("{}".format(i).replace("\n", ""))

first = 0
last = 0
sum = 0

for x in inputs:
    for i in range(len(x)):
        if x[i].isnumeric():
            first = x[i]
            break

    for i in range(len(x)):
        if x[len(x) - i - 1].isnumeric():
            last = x[len(x) - i - 1]
            break

    sum += int(first + last)

print(sum)

