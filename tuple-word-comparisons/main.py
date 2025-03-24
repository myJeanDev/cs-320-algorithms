import bisect


def input_validation(words, wordlist):
    if words is None or wordlist is None:
        return False
    if type(words) is not tuple or type(wordlist) is not tuple:
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


def find_word_in_list_binary_search(word, wordlist_as_list):
    index = bisect.bisect_left(wordlist_as_list, word)
    if index < len(wordlist_as_list) and wordlist_as_list[index] == word:
        return True
    return False


def find_differences_with_removal(words, wordlist):
    differences = []
    for word in words:
        is_found = find_word_in_list_binary_search(word, wordlist)
        if not is_found:
            differences.append(word)
    return tuple(differences)


def remove_duplicates(input):
    unique_dict = {}
    for each in input:
        unique_dict[each] = True
    return tuple(unique_dict.keys())


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
