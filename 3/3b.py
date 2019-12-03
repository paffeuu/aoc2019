wires = open("input.txt").readlines()
wires = [wire.split(",") for wire in wires]

positions = {}
for j in range(2):
    x, y = (0, 0)
    steps = 0
    for instruction in wires[j]:
        shift = int(instruction[1:])
        for i in range(shift):
            steps += 1
            if instruction[0] == 'R':
                x, y = x + 1, y
            elif instruction[0] == 'L':
                x, y = x - 1, y
            elif instruction[0] == 'D':
                x, y = x, y + 1
            elif instruction[0] == 'U':
                x, y = x, y - 1
            if (x, y) not in positions and j == 0:
                positions[(x, y)] = (steps, False)
            if (x, y) in positions and j == 1 and not positions[(x, y)][1]:
                positions[(x, y)] = (positions[(x, y)][0] + steps, True)

intersections = set()
for position, (steps, intersection) in positions.items():
    if intersection:
        intersections.add(steps)

print(min(intersections))
