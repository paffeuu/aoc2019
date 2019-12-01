file = open("input.txt")

modules = []
for line in file:
    modules.append(int(line.rstrip()))

sum = 0

for module in modules:
    while module > 0:
        module = int(module / 3) - 2
        if module > 0:
            sum += module

print(sum)