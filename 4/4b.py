min_pass = 183564
max_pass = 657474
counter = 0
digit = 6

for password in range(min_pass, max_pass + 1):
    password = str(password)
    ok = False
    ciphers = [0 for i in range(10)]
    for i in range(digit):
        ciphers[int(password[i])] += 1
    for j in range(10):
        if ciphers[j] == 2:
            ok = True
            break

    if ok:
        for i in range(digit - 1):
            if password[i] > password[i + 1]:
                ok = False
                break

    if ok:
        counter += 1

print(counter)