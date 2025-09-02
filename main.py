import sys
from stats import get_num_words, get_num_chars,format_dict
def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        
    return contents
def printer(formatted, num_words):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in formatted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        dictionary = get_num_chars(text)
        formatted = format_dict(dictionary)
        printer(formatted, num_words)
main()