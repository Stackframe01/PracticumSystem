import re
import nltk
from nltk import SnowballStemmer
from mysql_database import importer


def token_and_stem(text):
    stemmer = SnowballStemmer('russian')
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

    filtered_tokens = []
    for token in tokens:
        if re.search('[а-яА-Яa-zA-Z]', token):
            filtered_tokens.append(token)

    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def get_stopwords():
    stopwords = nltk.corpus.stopwords.words('russian')
    stopwords.extend(nltk.corpus.stopwords.words('english'))
    stopwords.extend(set(importer.get_stopwords_russian()))
    stopwords.extend(set(importer.get_stopwords_english()))

    return stopwords


def get_words(dataset):
    key_words = []
    for el in dataset:
        key_words.extend(token_and_stem(el))

    return list(set(key_words))


if __name__ == '__main__':
    pass
