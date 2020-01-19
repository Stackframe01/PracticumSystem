import re
import nltk
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

def clustering():
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

    '''
    # Обычная сортировка и вывод обработнных данных
    from collections import Counter

    new_arr = []
    for i in predataset['Required skill']:
        new_arr.extend(token_and_stem(i))

    sorted_skills = {k: v for k, v in sorted(Counter(predataset['Required skill']).items(), key=lambda item: item[1], reverse=True)}

    with open('data/{}.csv'.format('stem_sorted_key_skills'), 'w') as f_out:
        f_out.write(';Required skill\n')
        for i in range(len(sorted_skills)):
            f_out.write('{};{};{}\n'.format(i, list(sorted_skills.keys())[i], list(sorted_skills.values())[i]))
        f_out.close()
    '''

    vec = TfidfVectorizer(max_df=0.8, max_features=10000, min_df=0.01, stop_words=stopwords, use_idf=True, tokenizer=token_and_stem, ngram_range=(1,3))
    vec.fit(df['Required skill'])
    features = vec.transform(df['Required skill'])

    kmeans = MiniBatchKMeans(n_clusters=10, random_state=0)
    kmeans.fit(features)
    kmeans.predict(features)
    kmeans.labels_

    print(kmeans.labels_.tolist())

    pca = PCA(n_components=2, random_state=0)
    reduced_features = pca.fit_transform(features.toarray())
    reduced_cluster_centers = pca.transform(kmeans.cluster_centers_)

    print(silhouette_score(features, labels=kmeans.predict(features)))

    plt.scatter(reduced_features[:,0], reduced_features[:,1], c=kmeans.predict(features))
    plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')
    plt.show()

if __name__ == "__main__":
    clustering() # pass