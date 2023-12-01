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
            if  x[i + 1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or x[i + 2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
                break
            if numbers[num] in x[i:i + 5]:
                return str(num + 1)
            
def check_word_backwards(x):
    for i in range(len(x)):
        print(x[len(x) - i - 5:len(x) - i])
        if x[len(x) - i - 1].isnumeric():
            return x[len(x) - i - 1]
        for num in range(len(numbers)):
            if  x[len(x) - i - 1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or x[len(x) - i - 2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
                break
            if numbers[num] in x[len(x) - i - 5:len(x) - i]:
                return str(num + 1)
                
write = open("other_sums.txt", "w") 

for x in inputs:
    first = check_word_forwards(x)
    last = check_word_backwards(x)

    write.write(first + last + "\n")
            
    sum += int(first + last)

print(sum)

write.close()
