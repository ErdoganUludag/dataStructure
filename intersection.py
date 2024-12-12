def finding_intersection(array1, array2):
    intersection = []
    for num in array1:
        if num in array2 and num not in intersection:
            intersection.append(num)
    return intersection


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = finding_intersection(list1, list2)
print(intersection)


def find_intersection(array1, array2):
    intersection = list(set(array1) & set(array2))
    return intersection


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = find_intersection(list1, list2)
