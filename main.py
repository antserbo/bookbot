from stats import get_book_words, get_character_count
import sys


def get_book_text(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        file_contents = f.read()

        return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        file_p = sys.argv[1]

        file_content = get_book_text(file_p)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(get_book_words(file_content))
        print("--------- Character Count -------")
        char_dict = get_character_count(file_content)
        sorted_chars = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
        for char, count in sorted_chars.items():
            if char == ' ':
                display_char = '<SPACE>'
            elif char == '\n':
                display_char = '<NEWLINE>'
            else:
                display_char = char
            print(f"{display_char}: {count}")
        print("============= END ===============")


if __name__ == '__main__':
    main()
