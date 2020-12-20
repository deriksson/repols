def insort_any_type_left(sorted_list, list_item, less_than=lambda lhs, rhs: lhs < rhs):
    """Insert a list item into a sorted list, keeping the list sorted."""
    low = 0
    high = len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if less_than(sorted_list[mid], list_item):
            low = mid + 1
        else:
            high = mid

    sorted_list.insert(low, list_item)
