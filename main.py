def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)  
    character_dictionary = get_character_count(text)
    list = create_list(character_dictionary)
    sentences = create_sentences(list)
    report = create_report(book_path, words, sentences)
    return report
 
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    character_count = {}
    characters = list(text.lower())
    for character in characters:
        if character.isalpha():
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1
    return character_count

def sort_on(character_dictionary):
    return character_dictionary["num"]

def create_list(character_dictionary):
    character_list = [{"char": character, "num": number} for character, number in character_dictionary.items()]
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def create_sentences(list):
    sentences = []
    for l in list:
        sentences.append(f"The '{l['char']}' character was found {l['num']} times")
    return sentences

def create_report(path, words, characters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words are contained in this book")
    print()
    print('\n'.join(characters))
    print("--- End report ---")
    

main() 