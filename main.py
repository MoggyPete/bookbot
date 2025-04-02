import sys
from stats import count_chars
from stats import count_words
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_counts = count_chars(text)
    sorted_chars = chars_dict_to_sorted_list(character_counts)
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at ")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print ("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
