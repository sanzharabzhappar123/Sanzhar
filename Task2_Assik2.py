a = input()
b = input()

b_len = len(b)
a_len = len(a)

b_shifts = set()
for i in range(b_len):
    shift = b[i:] + b[:i]
    b_shifts.add(shift)

count = 0

for i in range(a_len - b_len + 1):
    sub = a[i: i + b_len]

    if sub in b_shifts:
        count += 1

print(count)