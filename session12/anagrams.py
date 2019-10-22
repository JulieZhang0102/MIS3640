def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    f = open(path_to_file)
    words = []
    for line in f:
        word = line.strip()
        words.append(word)
    return words


def list_to_dict(words):
    """
    convert a list of words to a dictionary and return it.
    The dictionary should be like:
    {'aedlts': ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']}
    """
    d = {}
    for word in words:
        fingerprint = "".join(sorted(word))
        # print(type(word), word)
        # print(type(fingerprint), fingerprint)
        if fingerprint not in d:
            d[fingerprint] = [word]
        else:
            d[fingerprint].append(word)
    return d


def print_anagrams(word_dict, n_words_in_anagram=1):
    """
    prints all the anagrams with more than one word
    """
    for v in word_dict.values():
        if len(v) > n_words_in_anagram:
            print(v)

def create_new_dict(old_dict):
    '''
    create a new dictionary, key is number, value is the anagrams with the same number of words
    return the new dictionary
    '''
    d = dict()
    for v in old_dict.values():
        k = len(v)
        if k not in d:
            d[k] = [v]
        else:
            d[k].append(v)
    return d

def print_anagrams_this_way(words_dict):
    '''
    words_dict is a dictionary with integer (key) : list of word lists (value) pairs
    print the list of word lists in descending order of integers
    '''
    for k in sorted(words_dict.keys(), reverse=True):
        print(k, words_dict[k])

def main():
    # path_to_words_file = "session09/words.txt"
    # words_list = read_file_to_list(path_to_words_file)
    # print(len(words_list))
    # print(words_list[:20])
    # print(words_list[-20:])

    words_list = [
        "generating",
        "deltas",
        "retainers",
        "desalt",
        "lasted",
        "salted",
        "slated",
        "staled",
        "ternaries",
        "greatening",
        "brian",
    ]

    anagrams = list_to_dict(words_list)
    # print(anagrams)
    # print_anagrams(anagrams, n_words_in_anagram=3)

    new_dict = create_new_dict(anagrams)
    print_anagrams_this_way(new_dict)



if __name__ == "__main__":
    main()