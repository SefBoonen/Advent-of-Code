input = ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

first = 0
last = 0
sum = 0

for x in input:
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