inputs = []
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

f = open("input.txt", "r")
for i in f.readlines():
    inputs.append("{}".format(i).replace("\n", ""))

first = 0
last = 0
sum = 0

def check_word_forwards(x):
    for i in range(len(x)):
        if x[i].isnumeric():
            return x[i]
        for num in range(len(numbers)):
            if numbers[num] in x[i:i + 5]:
                return str(num + 1)
            
def check_word_backwards(x):
    for i in range(len(x)):
        if x[len(x) - i - 1].isnumeric():
            return x[len(x) - i - 1]
        for num in range(len(numbers)):
            print(x[len(x) - i - 5:len(x) - i])
            if numbers[num] in x[len(x) - i - 5:len(x) - i]:
                return str(num + 1)
                

for x in inputs:
    print(x)
    first = check_word_forwards(x)
    last = check_word_backwards(x)
    print(first + last)
            
    sum += int(first + last)

print(sum)

