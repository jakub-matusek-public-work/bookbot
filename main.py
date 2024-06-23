def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print("The book contains",number_of_words(text),"words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

main()