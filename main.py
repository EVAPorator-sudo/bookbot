def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(wordcount(file_contents))
        #print(chartotal(file_contents))
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount(file_contents)} words found in the document")
        char_dict = chartotal(file_contents)
        for key in char_dict:
            print(f"the '{key}' character was found {char_dict[key]} times")
        print("--- End report ---")
            

def wordcount(file):
    return len(file.split())

def chartotal(file):
    character_count = {}
    file = file.lower()
    for char in file:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
    
    
main()
