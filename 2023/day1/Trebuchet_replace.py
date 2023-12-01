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
        for num in range(len(numbers)):
            if numbers[num] in x[i:i + 5]:
                x = x.replace(numbers[num], str(num + 1), 1)
    
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
