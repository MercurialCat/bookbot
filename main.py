def count_characters(character): #This is to give us a total character count in any given text file.
    character_dict = {}
    lowered_string = character.lower()
    for character in lowered_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def count_words(text):    #This is to give us a total word count of any given text file.
    words = text.split()
    return len(words)

#def read_file(file_path): #This is used to read any given text file
#    with open(file_path, "r") as f:
#        return f.read()

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents) 

    word_count = count_words(file_contents)
    print(f"The book contains {word_count}")
    
    character_count = count_characters(file_contents)
    print(character_count)

if __name__ == "__main__":
    main()