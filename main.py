import sys
from stats import get_num_words
from stats import get_num_chars
from stats import order_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ----------")
    get_num_words(get_book_text(book_filepath))
    print("--------- Character Count -------")
    order_char_counts(get_num_chars(get_book_text(book_filepath)))
    
def get_book_text(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        return text

if __name__ == "__main__":
    main()