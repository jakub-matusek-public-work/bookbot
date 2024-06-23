def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print("The book contains",number_of_words(text),"words")
    print("The frequency of letters is:",frequency_of_letters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def frequency_of_letters(text):
    frequency_dictionary = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
        }
    for letter in text:
        if letter.isalpha():
            frequency_dictionary[letter.lower()] += 1
    return frequency_dictionary

main()