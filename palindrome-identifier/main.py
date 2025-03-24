run_count = 0

def is_trivial(pattern) -> bool:
    return len(pattern) <= 2


def split_in_half(pattern) -> list[list]:
    center = int(len(pattern) / 2)
    left_side = pattern[:center]
    right_side = pattern[center:]
    return [left_side, right_side]


def reverse(pattern) -> list:
    return pattern[::-1]


def remove_one_element(left, right):
    length = min(len(left), len(right))
    has_removed = False
    for i in range(length - 1):
        if left[i] != right[i] and not has_removed:
            has_removed = remove_if_neighbor_can_replace(i, left, right)
    if not has_removed:
        right.pop(-1)


def remove_if_neighbor_can_replace(i, left, right):
    if i + 1 < len(left) and left[i + 1] == right[i]:
        if len(left) >= len(right):
            left.pop(i)
            return True
    if i + 1 < len(right) and right[i + 1] == left[i]:
        if len(right) >= len(left):
            right.pop(i)
            return True


def is_palindrome(pattern) -> bool:
    return pattern == pattern[::-1]


def find_palindrome(pattern) -> tuple | None:
    global run_count
    if run_count > 1:
        return None
    run_count += 1
    if type(pattern) is not tuple or is_trivial(pattern):
        return None
    
    pattern_split = split_in_half(list(pattern))
    left, right = pattern_split[0], reverse(pattern_split[1])
    if is_palindrome(left + reverse(right)):
        right.pop(-1)
    else:
        remove_one_element(left, right)
    palindrome = left + reverse(right)

    if is_palindrome(palindrome):
        print("we pallin")
        return tuple(palindrome)
    return find_palindrome(tuple(reverse(list(pattern))))


def test_find_palindrome():
    pattern = (2,1,2,3,3,2,1)
    print(pattern, find_palindrome(pattern), is_palindrome(find_palindrome(pattern)))


test_find_palindrome()
