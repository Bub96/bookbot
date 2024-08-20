def main():
    book_path = 'books/frankenstein.txt'
    txt = get_book_text(book_path)
    print(txt)
    print(num_of_words(txt))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(book):
    return (len(book))




main()