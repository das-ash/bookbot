import sys
from stats import no_of_words, no_of_characters, sorted_dic

def get_book_text(file_path):
    with open(file_path)  as f:
        file_content = f.read()
    return file_content
 


def main():
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    n_words = no_of_words(get_book_text(book_path))
    n_chars = no_of_characters(get_book_text(book_path))
    s_dict = (sorted_dic(n_chars))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for i in s_dict:
        dict = i
        print(f"{dict["char"]}: {dict["num"]}")

main()