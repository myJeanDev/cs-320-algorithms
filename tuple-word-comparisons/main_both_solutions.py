"""
- solution is O(n * log(n))
- words and wordlist will ALWAYS have the same length
- You may not use Python set operations
- If a word appears in words multiple times and is in wordlist, you must not return it in the list of new words.
- to sort without using case: sorted(unsorted_list, key=str.casefold)
"""
import bisect


operation_count = 0


def input_validation(words, wordlist):
    if words == None or wordlist == None:
        return False
    if not type(words) == tuple or not type(wordlist) == tuple:
        return False
    return True


def tuple_to_lower_case(input) -> tuple:
    # make a new list because tuples are immutable
    input_as_list = list(input)
    for i in range(len(input_as_list)):
        input_as_list[i] = input_as_list[i].lower()
    return tuple(input_as_list)


def sort_tuple_by_word(input: tuple) -> tuple:
    return tuple(sorted(list(input)))


def find_differences_naive(words, wordlist):
    operation_count = 0
    differences = []
    for each in words:
        found = False
        for every in wordlist:
            operation_count += 1
            if each == every:
                found = True
                break
        if not found:
            differences.append(each)
    print("[find_differences_naive]: completed with ", operation_count, " operations")
    return tuple(differences)


# this is basically the inside loop
def find_word_in_list(word, wordlist_as_list, start):
    step = start
    while step < len(wordlist_as_list):
        if word == wordlist_as_list[step]:
            # we found the word
            return True, step + 1
        elif word > wordlist_as_list[step]:
            # we can move our pointer forwards
            step += 1
        else:
            break
    return False, start


def find_word_in_list_binary_search(word, wordlist_as_list):
    index = bisect.bisect_left(wordlist_as_list, word)
    if index < len(wordlist_as_list) and wordlist_as_list[index] == word:
        return True, index + 1
    return False, index


def find_differences_with_removal(words, wordlist):
    wordlist_as_list = list(wordlist)
    differences = []
    start = 0
    for word in words:
        is_found, start = find_word_in_list(word, wordlist_as_list, start)
        if not is_found:
            differences.append(word)
    return tuple(differences)


def remove_duplicates(input):
    unique_list = []
    for each in list(input):
        if each not in unique_list:
            unique_list.append(each)
    return tuple(unique_list)


def new_words(words, wordlist) -> None | tuple:
    # Input validation
    if not input_validation(words, wordlist):
        return None
    # Convert all elements in words and wordlist to lowercase
    words = tuple_to_lower_case(words)
    wordlist = tuple_to_lower_case(wordlist)
    
    # sort tuples by word
    words = sort_tuple_by_word(words)
    wordlist = sort_tuple_by_word(wordlist)

    # remove duplicates
    words = remove_duplicates(words)
    wordlist = remove_duplicates(wordlist)

    # return the tuple of elements that exist within 'words' but not within 'wordlist'
    return find_differences_with_removal(words, wordlist)


def new_words_naive(words, wordlist) -> None | tuple:
    # Input validation
    if not input_validation(words, wordlist):
        return None
    # Convert all elements in words and wordlist to lowercase
    words = tuple_to_lower_case(words)
    wordlist = tuple_to_lower_case(wordlist)
    
    # sort tuples by word
    words = sort_tuple_by_word(words)
    wordlist = sort_tuple_by_word(wordlist)

    # remove duplicates
    words = remove_duplicates(words)
    wordlist = remove_duplicates(wordlist)

    # return the tuple of elements that exist within 'words' but not within 'wordlist'
    return find_differences_naive(words, wordlist)


def test_new_words(words, wordlist):
    input_size = max(len(words), len(wordlist))
    expected = tuple(set(words) - set(wordlist))
    expected = sort_tuple_by_word(expected)
    result = new_words(words, wordlist)
    result_naive = new_words_naive(words, wordlist)
    
    global operation_count
    operation_count = 0
    print("Input size [", input_size, "]")
    print("Naive Solution [", operation_count, "] operations", expected, "==", result)
    operation_count = 0
    print("Naive Solution: ")


test_tuple_words = ("crafting bench", "apple", "apple", "door", "wood", "pickaxe")
test_tuple_words_two = ("apple", "glowstone", "fish", "wood", "flint", "crafting bench")
test_tuple_wordlist = ("apple", "glowstone", "fish", "wood", "flint", "crafting bench")
test_new_words(test_tuple_words, test_tuple_wordlist)
test_new_words(test_tuple_words_two, test_tuple_wordlist)
