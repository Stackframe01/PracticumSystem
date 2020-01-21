import re
import nltk
import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf(predataset):
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
    stopwords.extend(set(pd.read_csv('data/vocabularies/stopwords_russian.csv')['Stopword']))
    
    '''
    # Можно обработать, чтобы не было предупреждения
    # Если обрабатывать так, то некоторые слова сокращаются до одной буквы
    new_stopwords = []
    for i in stopwords:
        new_stopwords.extend(token_and_stem(i))
    stopwords = new_stopwords
    new_stopwords = []
    for i in stopwords:
        new_stopwords.extend(token_and_stem(i))
    stopwords = new_stopwords
    '''

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.01, stop_words=stopwords, use_idf=True, tokenizer=token_and_stem, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(predataset)

    return tfidf_matrix

def k_means(tfidf_matrix, n_clusters=250):
    return KMeans(n_clusters=n_clusters).fit(tfidf_matrix)

def dbscan(tfidf_matrix, eps=0.3, min_samples=10):
    return DBSCAN(eps=eps, min_samples=min_samples).fit(tfidf_matrix)

def k_means_visualization(file_name, tfidf_matrix, km):
    pca = PCA(n_components=2, random_state=0)
    reduced_features = pca.fit_transform(tfidf_matrix.toarray())
    reduced_cluster_centers = pca.transform(km.cluster_centers_)

    plt.scatter(reduced_features[:,0], reduced_features[:,1], c=km.predict(tfidf_matrix))
    plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')
    plt.savefig('visualization/{}'.format(file_name))

def dbscan_visualization(file_name, tfidf_matrix, db):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True

    unique_labels = set(db.labels_)
    colors = plt.cm.get_cmap('Spectral')(np.linspace(0, 1, len(unique_labels)))

    for k, col in zip(unique_labels, colors):
        if k != -1:
            col = [0, 0, 0, 1]
        class_member_mask = (db.labels_ == k)
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=14)
        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=6)

    plt.savefig('visualization/{}'.format(file_name))

def to_csv(file_name, predataset, cluster):
    out = dict(zip(predataset, cluster.labels_.tolist()))

    new_out = {}
    for key, value in out.items():
        if value not in new_out:
            new_out[value] = [key]
        else:
            new_out[value].append(key)

    new_out = {k: v for k, v in sorted(new_out.items(), key=lambda item: len(item[1]), reverse=True)}
    
    for key, value in new_out.items():
        new_out[key] = str(new_out[key])

    framedb = pd.DataFrame({'Skills': list(new_out.values()), 'Cluster': list(new_out.keys())}, columns = ['Skills', 'Cluster'])
    framedb.to_csv('data/processed_data/{}.csv'.format(file_name), sep=';')

def clustering():
    # Debug
    print('Ввод данных')
    predataset = pd.read_csv('data/raw_data/big_dataset.csv', sep = ';', index_col=0)
    print('Формирование матрицы TF-IDF')
    tfidf_matrix = get_tfidf(predataset['Required skill'])

    print('Обработка: K-Means')
    km = k_means(tfidf_matrix)
    print('Визуализация: K-Means')
    k_means_visualization('k_means.jpg', tfidf_matrix, km)
    print('Вывод данных: K-Means')
    to_csv('sorted_k_means', predataset['Required skill'].tolist(), km)
    
    print('Обработка: DBSCAN')
    db = dbscan(tfidf_matrix)
    print('Визуализация: DBSCAN')
    dbscan_visualization('dbscan.jpg', tfidf_matrix, db)
    print('Вывод данных: DBSCAN')
    to_csv('sorted_dbscan', predataset['Required skill'].tolist(), db)

if __name__ == "__main__":
    clustering() # pass
