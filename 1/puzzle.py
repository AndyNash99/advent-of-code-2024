from collections import Counter

with open('input.txt') as file:

    list_1 = []
    list_2 = []
    for line in file.readlines():
        s1, s2 = line.split()
        list_1.append(int(s1))
        list_2.append(int(s2))

    # part 1
    # list_1.sort()
    # list_2.sort()
    # print(sum(abs(n1 - n2) for n1, n2 in zip(list_1, list_2)))

    # part 2
    counter = Counter(list_2)
    similarity_score = 0
    for item in list_1:
        similarity_score += item * counter.get(item, 0)

    print(similarity_score)
