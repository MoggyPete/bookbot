def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    letters = {}
    lower = text.lower()  
    for char in lower:
        letters[char] = letters.get(char, 0) + 1
    return letters

def chars_dict_to_sorted_list(char_dict):
    result = []
    for char, count in char_dict.items():
        result.append({"char": char, "count": count})
    def sort_on(dict_item):
        return dict_item["count"]
    result.sort(reverse=True, key=sort_on)
    return result


  
