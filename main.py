def main():
    book_path = 'books/frankenstein.txt'
    txt = get_book_text(book_path)
    print(num_char(txt))
    print(num_of_words(txt))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(book):
    return (len(book))

def num_char(book):
    letters={}
    text = book.lower()
    for t in text:
        if t in letters:
            letters[t] += 1
        else:
            letters[t] = 1
    return letters

main()