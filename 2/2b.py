memory = open("input.txt").readline()
memory = memory.split(",")
memory = list(map(int, memory))

for noun in range(100):
    for verb in range(100):
        values = memory.copy()
        values[1] = noun
        values[2] = verb
        for i in range(0, len(values), 4):
            if values[i] == 1:
                values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
            if values[i] == 2:
                values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
            if values[i] == 99:
                break
        if values[0] == 19690720:
            output = 100 * noun + verb
            print(output)
            exit(0)
