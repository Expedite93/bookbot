def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    words = file_contents.split()
    total = len(words)
    print(f"{total} words in book")

    new_text = file_contents.lower()
    characters = {}
    for character in new_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    print(characters)
    char_list = [{"char": char, "num": count} for char, count in characters.items()]
    for character in characters:
main()
