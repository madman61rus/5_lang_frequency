import sys
import os
import re

def load_data(filepath):
    result_dict = {}

    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as data_file:
        for line in data_file:
            tmp_line = (re.sub(r'[^\w]',' ',line)).split()
            for word in tmp_line:
                if word in result_dict:
                    result_dict[word] += 1
                else:
                    result_dict[word] = 1
        return result_dict


def get_most_frequent_words(text):
    result = [(x[0],x[1]) for x in sorted(text.items() , key = lambda x : x[1], reverse = True)][:10]
    return (result)

if __name__ == '__main__':

    if (sys.argv[1]):
        words = load_data(sys.argv[1])
    else:
        print('''Укажите, пожалуйста, имя файла с данными.
                    Пример:
                        lang_frequency.py book.txt''')

    most_frequent_words = get_most_frequent_words(words)

    for word in most_frequent_words:
        print('Слово "', word[0],'" повторяется ', word[1], ' раз')


