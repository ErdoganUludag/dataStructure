array = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 99, 99, 1, 1, 2, 3]


def detective_duplication(array):
    seen = set()
    duplicate = set()
    for num in array:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    return list(seen)


result = detective_duplication(array)
detective_duplication(array)
print(result)
