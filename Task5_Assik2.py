valid_letters = "ABCEHKMOPTXY"
valid_digits = "0123456789"

n = int(input())

for i in range(n):
    plate = input()

    if len(plate) != 6:
        print("No")
        continue

    is_valid = True

    if plate[0] not in valid_letters:
        is_valid = False
    elif plate[4] not in valid_letters:
        is_valid = False
    elif plate[5] not in valid_letters:
        is_valid = False

    elif plate[1] not in valid_digits:
        is_valid = False
    elif plate[2] not in valid_digits:
        is_valid = False
    elif plate[3] not in valid_digits:
        is_valid = False

    if is_valid:
        print("Yes")
    else:
        print("No")