from stats import get_num_words, get_char_counts, sort_char_counts
import sys


def get_book_text(book_path):
    book_text = ""
    with open(book_path) as f:
        book_text = f.read()
    return book_text


def print_header(h, sep="=", length=33):
    h_strip = h.strip()
    h_pad = f" {h_strip} "
    h_len = len(h_pad)
    r = length - h_len
    if r % 2 == 1:
        #    print(f"r: {r}, r floor: {r//2}")
        h_str = sep * (r // 2) + h_pad + sep * ((r // 2) + 1)
    else:
        h_str = sep * (r // 2) + h_pad + sep * (r // 2)
    print(h_str)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    wc = get_num_words(text)
    char_dict = get_char_counts(text)
    sorted_chars = sort_char_counts(char_dict)

    print_header("BOOKBOT", "=")
    print(f"Analyzing book found at {book_path}...")
    print_header("Word Count", "-")
    print(f"Found {wc} total words")
    print_header("Character Count", "-")

    for i in sorted_chars:
        print(f"{i['char']}: {i['num']}")


if __name__ == "__main__":
    main()
