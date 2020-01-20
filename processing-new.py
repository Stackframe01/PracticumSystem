import re
import nltk
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
    
    # Можно обработать, чтобы не было предупреждения
    stopwords = nltk.corpus.stopwords.words('russian')
    stopwords.extend(set(pd.read_csv('data/vocabularies/stopwords_russian.csv')['Stopword']))

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.01, stop_words=stopwords, use_idf=True, tokenizer=token_and_stem, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(predataset['Required skill'])

    return tfidf_matrix

def k_means(tfidf_matrix):
    return KMeans(n_clusters=10).fit(tfidf_matrix)

def dbscan(tfidf_matrix):
    return DBSCAN(eps=0.3, min_samples=10).fit(tfidf_matrix)

def k_means_visualization(tfidf_matrix, km):
    pca = PCA(n_components=2, random_state=0)
    reduced_features = pca.fit_transform(tfidf_matrix.toarray())
    reduced_cluster_centers = pca.transform(km.cluster_centers_)

    plt.scatter(reduced_features[:,0], reduced_features[:,1], c=km.predict(tfidf_matrix))
    plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')
    plt.savefig('visualization/k_means.jpg')

def dbscan_visualization(tfidf_matrix, db):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True

    unique_labels = set(db.labels_)
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]
        class_member_mask = (db.labels_ == k)
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=14)
        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),markeredgecolor='k', markersize=6)

    plt.savefig('visualization/dbscan.jpg')

def clustering(reqs=[]):
    # predataset = pd.DataFrame(reqs, columns='Required skill') # Работа с массивом для Release версии
    # nltk.download('punkt')
    # nltk.download('stopwords')

    print('Ввод данных')
    predataset = pd.read_csv('data/key_skills_and_requirements.csv', sep = ';', index_col=0)
    print('Формирование матрицы TF-IDF')
    tfidf_matrix = get_tfidf(predataset)

    print('Обработка: K-Means')
    km = k_means(tfidf_matrix)
    print('Визуализация: K-Means')
    k_means_visualization(tfidf_matrix, km)

    '''
    print('Вывод данных: K-Means')
    out = { 'Skills': predataset['Required skill'], 'cluster': km.labels_.tolist() }
    framekm = pd.DataFrame(out, index = [km.labels_.tolist()], columns = ['Skills', 'cluster'])
    framekm.to_csv('data/k_means', sep=';')
    '''

    print('Обработка: DBSCAN')
    db = dbscan(tfidf_matrix)
    print('Визуализация: DBSCAN')
    dbscan_visualization(tfidf_matrix, db)

    '''
    print('Вывод данных: DBSCAN')
    out = { 'Skills': predataset['Required skill'], 'cluster': db.labels_.tolist() }
    framedb = pd.DataFrame(out, index = [db.labels_.tolist()], columns = ['Skills', 'cluster'])
    framedb.to_csv('data/dbscan', sep=';')
    '''

if __name__ == "__main__":
    clustering() # pass
