def all_eq(lst):
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    new_list = []

    for s in lst:
        diff = max_len - len(s)

        new_s = s + "_" * diff

        new_list.append(new_s)

    return new_list

input_list = ["a", "aa", "aaaaa", "zz"]
print(all_eq(input_list))