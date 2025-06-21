def no_of_words(book_content):
    words_in_book = book_content.split()
    no_of_words = 0
    for i in words_in_book:
        no_of_words += 1
    return no_of_words

def no_of_characters(book_content):
    book_lcase = book_content.lower()
    char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                  'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,'n': 0, 
                  'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,'t': 0, 'u': 0, 
                  'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0 ,'-': 0, ',': 0
                  ,'.': 0}
    for i in book_lcase:
        if i in char_count:
            char_count[i] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sorted_dic(dictio):
    dict_list = []
    for i in dictio:
        dict_list.append({'char':i,'num':dictio[i]})

    dict_list.sort(reverse = True, key=sort_on)
    
    return dict_list