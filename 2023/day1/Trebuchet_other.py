inputs = []
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

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
        for num in range(len(numbers)):
            if x[i:i + 5] in numbers[num]:
                first = num + 1
                print(x[i:i + 5])
            




    print(first)

print(sum)

