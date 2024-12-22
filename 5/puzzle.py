ordering = {}
updates = None

def update_in_right_order(update):
    for i, page in enumerate(update):
        invalid_pages = ordering[page]
        for j in range(i + 1, len(update)):
            if update[j] in invalid_pages:
                return False

    return True


def order_update(update):
    for i in range(len(update)):
        swapped = True
        while swapped:
            invalid_pages = ordering[update[i]]
            swapped = False
            for j in range(i + 1, len(update)):
                if update[j] in invalid_pages:
                    update[i], update[j] = update[j], update[i]
                    swapped = True
                    break


with open('input.txt') as file:
    lines = file.readlines()
    idx = lines.index('\n')
    ordering_rules = lines[:idx]
    updates = [[int(page) for page in line.replace('\n', '').split(',')] for line in lines[idx + 1:]]
    for rule in ordering_rules:
        rule = rule.replace('\n', '')
        value, key = rule.split('|')
        key = int(key)
        value = int(value)
        if key not in ordering:
            ordering[key] = set()
        ordering[key].add(value)

correct_sum = 0
incorrect_sum = 0
for update in updates:
    if update_in_right_order(update):
        correct_sum += update[len(update) // 2]
    else:
        order_update(update)
        incorrect_sum += update[len(update) // 2]

print(f'correct: {correct_sum}', f'incorrect: {incorrect_sum}')
