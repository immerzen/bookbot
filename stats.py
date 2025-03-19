def get_num_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def get_num_chars(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def order_char_counts(char_count):
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_char_count:
        print(f"{char}: {count}")