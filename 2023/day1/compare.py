other_sums = open("other_sums.txt", "r")
sum = open("sums.txt", "r")
internet = open("internet.txt", "r")

list_other_sums = other_sums.readlines()
list_sum = other_sums.readlines()
list_internet = other_sums.readlines()

for i in range(len(sum.readlines())):
    if sum.readlines()[i] != internet.readlines()[i]:
        print(sum.readlines()[i])