inputs = []
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

f = open("./2023/day1/input.txt", "r")
for i in f.readlines():
    inputs.append("{}".format(i).replace("\n", ""))

first = 0
last = 0
sum = 0

write = open("./2023/day1/replace.txt", "w")

for x in inputs:
    backwards = x

    for i in range(len(x)):
        for num in range(len(numbers)):
            if numbers[num] in x[i:i + 5]:
                x = x.replace(numbers[num], str(num + 1), 1)
    
    for i in range(len(x)):
        if x[i].isnumeric():
            first = x[i]
            break

    for i in range(len(backwards)):
        for num in range(len(numbers)):
            if numbers[num] in backwards[len(backwards) - i - 6:len(backwards) - i - 1]:
                backwards = backwards.replace(numbers[num], str(num + 1), 1)

    for i in range(len(backwards)):
        if backwards[len(backwards) - i - 1].isnumeric():
            last = backwards[len(backwards) - i - 1]
            break

    write.write(first + last + "\n")
            
    sum += int(first + last)

write.close()
print(sum)
