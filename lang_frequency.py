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
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return 0


def get_words_from_line(line):
    words_from_line = []
    if len(line) > 1:
        line = line.lower()
        words_from_line = re.findall(r'[^\W0-9_]+', line)
    return words_from_line


def treatment_data(file_data, word_amount):
    word_list = collections.Counter()
    for line in file_data:
            word_list.update(get_words_from_line(line))
    print(word_list.most_common(word_amount))


if __name__ == '__main__':
    word_amount = 10
    file_name = input_file_name()
    if file_exists(file_name) is None:
        print("Ошибка открытия файла")
    else:
        treatment_data(open(file_name, 'r'), word_amount)
