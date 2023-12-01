import re

# part two
my_sum = 0
digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def find_item(item, text):
    return [m.start() for m in re.finditer(f'(?={item})', text)]

internet = open("internet.txt", "w")

with open('input.txt') as file:
    for line in file:
        line = line.replace('\n', '').strip()
        indexes = []
        values = []
        for item in digit_map:
            
            if len(find_item(item, line))>0:
                indexes+=find_item(item, line)
                values+=[digit_map[item]]*len(find_item(item, line))

            if len(find_item(digit_map[item], line))>0:
                indexes+=find_item(digit_map[item], line)
                values+=[digit_map[item]]*len(find_item(digit_map[item], line))
        
        line_split = [v for _, v in sorted(zip(indexes, values))]

        if len(line_split) == 1:
            my_value = int(2*line_split[0])
            my_sum += my_value
            internet.write(str(my_value) + "\n")

        elif len(line_split)>1:
            my_value = int(line_split[0]+line_split[-1])
            my_sum += my_value
            internet.write(str(my_value) + "\n")

print(my_sum)