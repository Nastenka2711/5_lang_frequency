import collections
import re

c = collections.Counter()

def load_data(filepath):
    for line in filepath:
        words = re.split('[\s\0.,>:=?\\/\-\(\)\+\[\]\"\']+', line)
        get_most_frequent_words(words)
    return

def get_most_frequent_words(text):
    for word in text:
        word = word.lower()
        c[word] += 1

if __name__ == '__main__':
    load_data(open('list_words.txt','r'))
    print(c.most_common(10))

