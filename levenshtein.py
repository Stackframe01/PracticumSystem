import re
import nltk
import Levenshtein
import numpy as np
import pandas as pd
from collections import Counter
from nltk.stem.snowball import SnowballStemmer

df = pd.read_csv('data/key_skills_and_requirements.csv', sep = ';', index_col=0)
stemmer = SnowballStemmer('russian')

def token_and_stem(text):
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        for token in tokens:
            if re.search('[а-яА-Я]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        return stems

stopwords = nltk.corpus.stopwords.words('russian')
stopwords.extend(set(pd.read_csv('data/stopwords_russian.csv')['Stopword']))

new_arr = []
for i in df['Required skill']:
    new_arr.extend(token_and_stem(i))

sorted_skills = {k: v for k, v in sorted(Counter(df['Required skill']).items(), key=lambda item: item[1], reverse=True)}

keys = list(sorted_skills.keys())
values = list(sorted_skills.values())

'''
# Не реализовано
for i in range(len(keys) - 1):
    for j in range(len(keys) - i - 1):
        if (type(keys[j]) == list):
            if Levenshtein.distance(keys[j][0], keys[j + 1]) < 5:
                keys[j].append(keys[j + 1])
                values[j] += values[j + 1]
                del values[j + 1]
                del keys[j + 1]
        else:
            if Levenshtein.distance(keys[j], keys[j + 1]) < 5:
                keys[j] = [keys[j], keys[j + 1]]
                values[j] += values[j + 1]
                del values[j + 1]
                del keys[j + 1]
'''

with open('data/{}.csv'.format('sorted'), 'w') as f_out:
    f_out.write(';Required skill\n')
    for i in range(len(sorted_skills)):
        f_out.write('{};{};{}\n'.format(i, keys[i], values[i]))
    f_out.close()