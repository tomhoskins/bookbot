def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    return len(words)

def get_char_counts(text):
    chars = {}
    for char in text:
        key = char.lower()
        if key in chars:
            chars[key] += 1
            continue
        chars[key] = 1
    return chars

def sort_on_num(items):
    return items["num"]

def sort_char_counts(char_counts):
    sorted_char_counts = []
    for key,value in char_counts.items():
        sorted_char_counts.append({"char":key, "num":value})
    sorted_char_counts.sort(reverse=True,key=sort_on_num)
    return sorted_char_counts