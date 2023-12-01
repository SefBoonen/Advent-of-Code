other_sums = open("other_sums.txt", "r")
sum = open("sums.txt", "r")
internet = open("internet.txt", "r")
replace = open("replace.txt", "r")

list_other_sums = other_sums.readlines()
list_sum = sum.readlines()
list_internet = internet.readlines()
list_replace = replace.readlines()

for i in range(len(list_replace)):
    if list_internet[i] != list_other_sums[i]:
        print(i + 1)