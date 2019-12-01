file = open("input.txt")

modules = []
for line in file:
    modules.append(int(line.rstrip()))

sum = 0

for module in modules:
    module = int(module / 3) - 2
    sum += module

print(sum)