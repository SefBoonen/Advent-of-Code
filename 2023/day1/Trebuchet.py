inputs = []

f = open("input.txt", "r")
for i in f.readlines():
    inputs.append("{}".format(i).replace("\n", ""))

first = 0
last = 0
sum = 0

write = open("sums.txt", "w")

for x in inputs:
    word = ""
    for char in x:
        word += char
        word = word.replace("one", "1")
        word = word.replace("two", "2")
        word = word.replace("three", "3")
        word = word.replace("four", "4")
        word = word.replace("five", "5")
        word = word.replace("six", "6")
        word = word.replace("seven", "7")
        word = word.replace("eight", "8")
        word = word.replace("nine", "9")
    print(word)

    for i in range(len(word)):
        if word[i].isnumeric():
            first = word[i]
            break

    for i in range(len(word)):
        if word[len(word) - i - 1].isnumeric():
            last = word[len(word) - i - 1]
            break

    write.write(first + last + "\n")

    sum += int(first + last)

print(sum)

