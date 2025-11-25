import sys
from stats import get_num_words, get_book_text, get_char_counts, sort_char_counts

def print_report(book_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file[2:]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_file)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(get_book_text(book_file))
    sorted_char_counts = sort_char_counts(char_counts)
    for item in sorted_char_counts:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]
    print_report(book_filepath)

main()