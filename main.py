def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    characters_list = count_characters(text)
    characters_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"A total of: {words} words have been found")
    print("")

    for character in characters_list:
        print(f"The '{character['char']}' character was found {character['num']} times")
    
    print("")
    print("--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dir = {}
    low_char = text.lower()
    for char in low_char:
        if char.isalpha():
            if char in char_dir:    
                char_dir[char] += 1
            else:
                char_dir[char] = 1

    char_list = [{"char": char, "num": count} for char, count in char_dir.items()]
    return char_list

def sort_on(characters):
    return characters["num"]

main()