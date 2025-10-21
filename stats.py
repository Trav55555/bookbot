import string


def get_num_words(t):
    return len(t.split())


def get_char_counts(t):
    char_dict = {}

    for char in t:
        if char not in string.whitespace:
            c_low = char.lower()
            if c_low not in char_dict:
                char_dict[c_low] = 1
            else:
                char_dict[c_low] += 1
    return char_dict


def sort_char_counts(d):
    sorted = [{"char": k, "num": v} for k, v in d.items()]

    def get_count(item):
        return item["num"]

    sorted.sort(key=get_count, reverse=True)
    print(sorted)
    return sorted
