def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return list(dict.values())[0]

def convert_and_sort_dict(char_dict):
    char_list = [{char: count} for char, count in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

