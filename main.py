def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = count_string_words(text)
    charcount = count_string_chars(text)
    print(f"Wordcount: {wordcount}")
    print_list_of_tuples(sort_dict(charcount))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_string_words(str):
    return len(str.split())

def count_string_chars(str):
    lowercase_list = list(str.lower())
    char_count = {}
    for char in lowercase_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(dict):
    list_to_sort = []
    for entry in dict:
        if entry.isalpha():
            list_to_sort.append((entry,dict[entry]))

        list_to_sort.sort(reverse=True, key=lambda tup: tup[1])
    return list_to_sort
    
def print_list_of_tuples(lis):
    for entry in lis:
        print(f"{entry[0]}: {entry[1]}")


main()
