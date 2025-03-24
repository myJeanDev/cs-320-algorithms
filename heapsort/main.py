def max_heapify(elements, list_length, current_step):
    """
    Modifies a list of elements, calling the max_heapify() method to sort them into a max-heap. 

    Parameters:
    elements (list): A list of unsorted elements.
    list_length (int): Size of the unsorted list of elements.
    current_step (int): The current parent node to check its children.
    """
    # largest element
    largest = current_step
    # position of left child in list
    left = 2 * current_step + 1
    # position of right child in list
    right = 2 * current_step + 2

    # Left and right tree comparisons
    if left < list_length and elements[left] > elements[largest]:
        largest = left
    if right < list_length and elements[right] > elements[largest]:
        largest = right

    # Base Case
    if largest != current_step:
        # Swap those elements
        elements[current_step], elements[largest] = elements[largest], elements[current_step]
        # Recursive call
        max_heapify(elements, list_length, largest)


def build_max_heap(unsorted_list):
    """
    Modifies a list of elements, calling the max_heapify() method to sort them into a max-heap. 

    Parameters:
    unsorted_list (list): A list of unsorted elements.
    """
    list_length = len(unsorted_list)
    start = list_length // 2 - 1
    end = -1
    step = -1
    # for loop stepping backwards
    for i in range(start, end, step):
        max_heapify(unsorted_list, list_length, i)


def heapsort(hlist):  # Entry Point
    # input validation
    if hlist is None:
        return None
    if not hlist:
        return []
    
    # Create a copy of the list using list comprehension
    unsorted_list = hlist[:]
    build_max_heap(unsorted_list)

    start = len(unsorted_list) - 1
    end = -1
    step = -1
    sorted_list = []
    # This loop adds sorted elements to the sorted part of the list
    for i in range(start, end, step):
        sorted_list.append(unsorted_list[0])
        unsorted_list[0] = unsorted_list[i]
        max_heapify(unsorted_list, i, 0)

    # reverse it so the list is ordered lowest to highest
    return sorted_list[::-1]
