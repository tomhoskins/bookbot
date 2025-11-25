from stats import get_num_words, get_book_text, get_char_counts

def main():
    frankenstein_file = "./books/frankenstein.txt"
    num_words = get_num_words(frankenstein_file)
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(get_book_text(frankenstein_file))
    for key,value in char_counts.items():
        print(f"'{key}': {value}")

main()