def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print("-------------------")
    print(get_num_words(text))
    print("-------------------")
    counted_letters_dict = count_letters(text)
    print(counted_letters_dict)
    print_report(counted_letters_dict)



def get_num_words(example_text):
    list_of_words = example_text.split()
    return f"Anzahl der Wörter: {len(list_of_words)}"

def count_letters(example_text):
    list_of_words = example_text.split()
    list_of_lower_case_words = list()
    for word in list_of_words:
        list_of_lower_case_words.append(word.lower())
    dict_of_letter_nums = {}
    for word in list_of_lower_case_words:
        for letter in word:
            if letter in dict_of_letter_nums:
                dict_of_letter_nums[letter] += 1
            else:
                dict_of_letter_nums[letter] = 1
    return dict_of_letter_nums

def print_report(unsorted_dict):
    list_of_occ = list()
    for key, value in unsorted_dict.items():
        if key.isalpha() == True:
            list_of_occ.append(value)
    list_of_occ.sort(reverse=True)
    # print(list_of_occ)

    list_of_sorted_pairs = list()
    for occ in list_of_occ:
        for key, value in unsorted_dict.items():
            if value == occ:
                list_of_sorted_pairs.append({key:value})
    # print(list_of_sorted_pairs)
    
    for elem in list_of_sorted_pairs:
        for key, value in elem.items():
            print(f"The '{key}' character was found '{value}' times")
    print("--- End report ---")
    




def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


