def move_zeros(array):
    index = 0
    for num in array:
        if num != 0:
            array[index] = num
            index += 1
    while index < len(array):
        array[index] = 0
        index += 1


array = [0, 0, 0, 0, 1, 2, 3, 5, 6, 0, 9, 4, 2, 3, 0, 77, 9, 0]
move_zeros(array)
print(array)
