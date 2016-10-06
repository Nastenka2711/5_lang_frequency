import collections
import re
import os
import sys


def input_name_file():
    if len(sys.argv) == 1:
        name_file = input("Введите название файла  ")
    else:
        name_file = sys.argv[1]
    return name_file


def existence_file(filepath):
    if os.path.exists(name_file) and os.path.isfile(name_file):
        return 0
    else:
        return None


def treatment_data(filepath):
    final_list_words = collections.Counter()
    for line in filepath:
        if len(line) > 1:
            line = line.lower()
            subsidiary_regular_object = re.compile(r'\W+')
            words_from_line = subsidiary_regular_object.split(line)
            get_most_frequent_words(words_from_line, final_list_words)
    print(final_list_words.most_common(10))


def get_most_frequent_words(text_line, final_list_words):
    for word in text_line:
        final_list_words[word] += 1
    return(final_list_words)


if __name__ == '__main__':
    name_file = input_name_file()
    if existence_file(name_file) is None:
        print("Ошибка открытия файла")
    else:
        treatment_data(open(name_file, 'r'))
