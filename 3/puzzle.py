import re

with open('input.txt') as file:
    file_string = file.read()
    matches = re.findall(r'mul\(\d+,\d+\)', file_string)
    result = 0
    for match in matches:
        comma_idx = match.index(',')
        # n1 = match[4:comma_idx]
        # n2 = match[comma_idx + 1:len(match) - 1]
        # print(match, n1, n2)
        result += int(match[4:comma_idx]) * int(match[comma_idx + 1:len(match) - 1])

    print(result)
