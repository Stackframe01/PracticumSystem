import re
import nltk
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf(dataset):
    stemmer = SnowballStemmer('russian')

    def token_and_stem(text):
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

        filtered_tokens = []
        for token in tokens:
            if re.search('[а-яА-Яa-zA-Z]', token):
                filtered_tokens.append(token)

        stems = [stemmer.stem(t) for t in filtered_tokens]
        return stems
    
    stopwords = nltk.corpus.stopwords.words('russian')
    stopwords.extend(nltk.corpus.stopwords.words('english'))
    stopwords.extend(set(pd.read_csv('data/vocabularies/stopwords_russian.csv')['Stopword']))
    stopwords.extend(set(pd.read_csv('data/vocabularies/stopwords_english.csv')['Stopword']))

    tfidf_vectorizer = TfidfVectorizer(tokenizer=token_and_stem, stop_words=stopwords, min_df=0.01, token_pattern=r'[(?u)\b\w\w+\bа-яА-Я]+')
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)

    return tfidf_matrix.toarray()

def dbscan(tfidf_matrix, eps=0.01, min_samples=5, n_jobs=-1, leaf_size=100):
    return DBSCAN(eps=eps, min_samples=min_samples, n_jobs=n_jobs, leaf_size=leaf_size).fit(tfidf_matrix)

def to_csv(file_name, dataset, cluster):
    out = dict(zip(dataset, cluster.labels_.tolist()))

    new_out = {}
    for key, value in out.items():
        if value not in new_out:
            new_out[value] = [key]
        else:
            new_out[value].append(key)

    new_out = {k: v for k, v in sorted(new_out.items(), key=lambda item: len(item[1]), reverse=True)}
    
    framedb = pd.DataFrame({'Required skills': list(new_out.values())}, columns=['Required skills'])
    framedb.to_csv('data/processed_data/{}.csv'.format(file_name), sep=';')

if __name__ == "__main__":
    pass
