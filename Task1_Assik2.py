sequence = "<<<<>>--><--<<--<<>>>--><<<<<"
count = 0
arrow1 = ">>-->"
arrow2 = "<--<<"
length = len(sequence)
arrow_len = len(arrow1)

max_length=250

if length > max_length:
    print(f"the length is long")
    exit()

for i in range(length - arrow_len + 1):
    substring = sequence[i: i + arrow_len]

    if substring == arrow1 or substring == arrow2:
        count += 1

print(f"Общее количество стрелок: {count}")