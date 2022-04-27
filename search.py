from qsort import qsort


def binary_search(search_item, a_list: list) -> bool:
    ''' binary search takes two arguments - the search item and a list.
        an attempt is made to sort the list before search is performed '''
    try:
        START = 0
        a_sorted_list = qsort(a_list)
        end = len(a_sorted_list)
        mid_point = end // 2
        if len(a_sorted_list) == 1 and a_sorted_list[0] != search_item:
            return False
        elif search_item < a_sorted_list[mid_point]:
            return binary_search(search_item, a_sorted_list[START: mid_point])
        elif search_item > a_sorted_list[mid_point]:
            return binary_search(search_item, a_sorted_list[mid_point: end])
        else:
            return True
    except TypeError:
        print(f"type mismatch: unable to search for {type(search_item)} in list")
    except UnboundLocalError as err:
        print(err)
