import matplotlib.pyplot as plt

wires = open("input.txt").readlines()
wires = [wire.split(",") for wire in wires]

positions = {}
X = []
Y = []
for j in range(2):
    X.append([])
    Y.append([])
    x, y = (0, 0)
    for instruction in wires[j]:
        shift = int(instruction[1:])
        for i in range(shift):
            if instruction[0] == 'R':
                x, y = x + 1, y
            elif instruction[0] == 'L':
                x, y = x - 1, y
            elif instruction[0] == 'D':
                x, y = x, y + 1
            elif instruction[0] == 'U':
                x, y = x, y - 1
            X[j].append(x)
            Y[j].append(y)
            if (x, y) in positions and j == 1:
                positions[(x, y)] = True
            elif j == 0:
                positions[(x, y)] = False
intersections = set()

for position, intersection in positions.items():
    if intersection:
        intersections.add(position)

min_distance = 10000000
for x, y in intersections:
    if (abs(x) + abs(y)) < min_distance:
        min_distance = abs(x) + abs(y)

print(min_distance)

plt.plot(X[0], Y[0])
plt.plot(X[1], Y[1])
plt.grid()
plt.show()