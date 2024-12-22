def contains_word(puzzle, x, y, x_delta, y_delta, target):
    '''Tries to find target word in puzzle starting from coordinates x,y
    and moving in direction x_delta,y_delta.
    '''
    if not puzzle or not target:
        return False

    for i, char in enumerate(target):
        if x < 0 or y < 0 or x >= len(puzzle[0]) or y >= len(puzzle):
            return False

        if puzzle[y][x] != char:
            return False

        x += x_delta
        y += y_delta

    return True


puzzle = None
with open('input.txt') as file:
    puzzle = file.readlines()

count = 0
# directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
for y in range(0, len(puzzle)):
    for x in range(0, len(puzzle[0])):
        mas_count = 0
        for x_delta, y_delta in directions:
            if contains_word(puzzle, x - x_delta, y - y_delta, x_delta, y_delta, 'MAS'):
                mas_count += 1
        if mas_count == 2:
            count += 1

print(count)
