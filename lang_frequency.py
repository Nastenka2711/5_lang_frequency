import collections
import re
import os
import sys


def input_file_name():
    if len(sys.argv) == 1:
        file_name = input("Введите название файла  ")
    else:
        file_name = sys.argv[1]
    return file_name


def file_exists(filepath):
    return os.path.exists(filepath) and os.path.isfile(filepath)


def get_words_from_line(line):
    words_from_line = []
    line = line.lower()
    words_from_line = re.findall(r'[^\W0-9_]+', line)
    return words_from_line


def treat_data(file_data):
    word_list = collections.Counter()
    word_list.update(get_words_from_line(file_data.read()))
    return word_list


def open_file(file_name):
    with open(file_name, 'r') as file_data:
        return treat_data(file_data)

if __name__ == '__main__':
    word_amount = 10
    file_name = input_file_name()
    if not file_exists(file_name):
        print("Ошибка открытия файла")
    else:
        word_list = open_file(file_name)
        print(word_list.most_common(word_amount))
