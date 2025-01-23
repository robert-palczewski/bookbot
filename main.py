def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Number of words: {countWords(file_contents)}\n")
        printCharCount(countChars(file_contents))
        

def countWords(file_contents):
    words = file_contents.split()
    return len(words)

def countChars(file_contents):
    file_contents = file_contents.lower()
    char_count = {}
    for char in file_contents:
        if char.isalpha() == True:    
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        ## print(char_count)
    return char_count

def printCharCount(char_count):
    def sort_on(char_count):
        return char_count[1]
       
    char_count_list = list(char_count.items())
    char_count_list.sort(reverse=True, key=sort_on)
    for char in char_count_list:
        print(f"The '{char[0]}' was used {char[1]} times")

    ## countWords(file_contents)
    ## countChars(file_contents)

main()
