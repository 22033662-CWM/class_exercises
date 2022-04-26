def qsort(some_list: list) -> list:
    if some_list == []:
        return []
    try:
        pivot = some_list[0]
        left = qsort([x for x in some_list[1:] if x < pivot])
        right = qsort([x for x in some_list[1:] if x >= pivot])
        return left + [pivot] + right
    except TypeError:
        print('list contains mismatched types')

