values = open("input.txt").readline()
values = values.split(",")
values = list(map(int, values))

values[1] = 12
values[2] = 2

for i in range(0, len(values), 4):
    if values[i] == 1:
        values[values[i+3]] = values[values[i+1]] + values[values[i+2]]
    if values[i] == 2:
        values[values[i+3]] = values[values[i+1]] * values[values[i+2]]
    if values[i] == 99:
        break

print(values[0])
