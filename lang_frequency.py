import sys
import os
import re
import argparse
import collections

def load_data(filepath):
    '''Функция загружает текст из файла'''
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as data_file:
        text = data_file.read()

        return text

def handling_text(text):
    '''Функция разбивает текст на список слов'''

    return (re.sub(r'[^\w]',' ',text)).split()


def get_most_frequent_words(text,numbers_of_words=10):
    '''Функция вычисляет 10 самых часто используемых слов'''

    return collections.Counter(text).most_common(numbers_of_words)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="file to work with")
    args = parser.parse_args()

    text = load_data(args.file)
    words = handling_text(text)

    most_frequent_words = get_most_frequent_words(words)

    for word,times in most_frequent_words:
        print('Слово "', word,'" повторяется ', times , ' раз')


