import collections
import re
import os
import sys

c = collections.Counter()


def load_data(filepath):
    for line in filepath:
        if len(line) > 1:
            p = re.compile(r'\W+')
            words = p.split(line)
            get_most_frequent_words(words)
    return


def get_most_frequent_words(text):
    for word in text:
        word = word.lower()
        c[word] += 1


if __name__ == '__main__':
    if len(sys.argv) == 1:
        name_file = input("Введите название файла  ")
    else:
        name_file = sys.argv[1]
    if os.path.exists(name_file) and os.path.isfile(name_file):
        load_data(open(name_file, 'r'))
        print(c.most_common(10))
    else:
        print("Ошибка открытия файла")
