min_pass = 183564
max_pass = 657474
counter = 0
digit = 6

for password in range(min_pass, max_pass + 1):
    password = str(password)
    ok = False
    for i in range(digit - 1):
        if password[i] == password[i+1]:
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