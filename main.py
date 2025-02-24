from stats import count_words

import sys
if sys.argv != 2: 
    print("Usage: python3 main.py <path_to_book>") and sys.exit(1)
    
def count_characters(character): #This is to give us a total character count in any given text file.
    character_dict = {}
    lowered_string = character.lower()
    for character in lowered_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def print_report(char_count):
    char_list = []
    for letter in char_count:
        if letter.isalpha():
            letter_dict = {
                "character": letter,
                "num": char_count[letter]

            }
            char_list.append(letter_dict)

    def sort_on(dict):
        return dict["num"]
    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"{item['character']}: {item['num']}")


#def read_file(file_path): #This is used to read any given text file
#    with open(file_path, "r") as f:
#        return f.read()

def main():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    print(f"--- Begin report of {sys.argv[1]} ---") 
    

    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    print()
    character_count = count_characters(file_contents)
    pass
    print_report(character_count)
    print("--- End report ---")
if __name__ == "__main__":
    main()