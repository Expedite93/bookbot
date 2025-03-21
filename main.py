import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = convert_and_sort_dict(chars_dict)
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words, get_letter_count, convert_and_sort_dict
main()
