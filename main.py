import sys
import stats

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
        
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
        char_count = stats.count_chars(text)
        sorted_char_count = stats.sort_char_count(char_count)

        print(f"""============ BOOKBOT ============
        Analyzing book found at {book_path}...
        ----------- Word Count ----------
        Found {stats.count_words(text)} total words
        --------- Character Count -------""")
        
        for item in sorted_char_count:
          print(f"{item['char']}: {item['count']}")
        
        print("============= END ===============""")
    except FileNotFoundError:
        print(f"Error: The file at {book_path} could not be found.")
        sys.exit(1)
if __name__ == "__main__":
    main()
