import re
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans, KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, DBSCAN, OPTICS, Birch

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

    tfidf_vectorizer = TfidfVectorizer(tokenizer=token_and_stem, stop_words=stopwords, min_df=0.01)
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset)

    return tfidf_matrix

# АЛГОРИТМЫ

def mini_batch_k_means(tfidf_matrix, n_clusters=100, random_state=0):
    return MiniBatchKMeans(n_clusters=n_clusters, random_state=random_state).fit(tfidf_matrix)

def k_means(tfidf_matrix, n_clusters=100, random_state=0):
    return KMeans(n_clusters=n_clusters, random_state=random_state).fit(tfidf_matrix)

def affinity_propagation(tfidf_matrix, damping=0.5, max_iter=200, convergence_iter=15):
    return AffinityPropagation(damping=damping, max_iter=max_iter, convergence_iter=convergence_iter).fit(tfidf_matrix.toarray())

def mean_shift(tfidf_matrix, bandwidth=None):
    return MeanShift(bandwidth=bandwidth).fit(tfidf_matrix.toarray())

def spectral_clustering(tfidf_matrix, n_clusters=100, random_state=0):
    return SpectralClustering(n_clusters=n_clusters, random_state=random_state).fit(tfidf_matrix)

def agglomerative_clustering(tfidf_matrix, n_clusters=100):
    return AgglomerativeClustering(n_clusters=n_clusters).fit(tfidf_matrix.toarray())

def dbscan(tfidf_matrix, eps=0.05, min_samples=2):
    return DBSCAN(eps=eps, min_samples=min_samples).fit(tfidf_matrix)

def optics(tfidf_matrix, min_samples=5):
    return OPTICS(min_samples=min_samples).fit(tfidf_matrix.toarray())

def birch(tfidf_matrix, n_clusters=100, threshold=0.01):
    return Birch(n_clusters=n_clusters, threshold=threshold).fit(tfidf_matrix)

# ВИЗУАЛИЗАЦИЯ

def mini_batch_k_means_visualization(file_name, tfidf_matrix, mbkm):
    pca = PCA(n_components=2, random_state=0)
    reduced_features = pca.fit_transform(tfidf_matrix.toarray())
    plt.scatter(reduced_features[:,0], reduced_features[:,1], c=mbkm.predict(tfidf_matrix))

    '''
    # Вывод центров кластеров
    reduced_cluster_centers = pca.transform(km.cluster_centers_)
    plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')
    '''

    plt.savefig('visualization/{}'.format(file_name))

def k_means_visualization(file_name, tfidf_matrix, km):
    pca = PCA(n_components=2, random_state=0)
    reduced_features = pca.fit_transform(tfidf_matrix.toarray())
    plt.scatter(reduced_features[:,0], reduced_features[:,1], c=km.predict(tfidf_matrix))

    '''
    # Вывод центров кластеров
    reduced_cluster_centers = pca.transform(km.cluster_centers_)
    plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')
    '''

    plt.savefig('visualization/{}'.format(file_name))

def affinity_propagation_visualization(file_name, tfidf_matrix, ap):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=ap.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def mean_shift_visualization(file_name, tfidf_matrix, ms):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=ms.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def spectral_clustering_visualization(file_name, tfidf_matrix, sc):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=sc.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def agglomerative_clustering_visualization(file_name, tfidf_matrix, ac):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=ac.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def dbscan_visualization(file_name, tfidf_matrix, db):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=db.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def optics_visualization(file_name, tfidf_matrix, op):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=op.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def birch_visualization(file_name, tfidf_matrix, br):
    pca = PCA(n_components=2, random_state=0)
    X = pca.fit_transform(tfidf_matrix.toarray())

    plt.scatter(X[:,0], X[:,1],c=br.fit_predict(X), cmap='Paired')
    plt.savefig('visualization/{}'.format(file_name))

def to_csv(file_name, dataset, cluster):
    out = dict(zip(dataset, cluster.labels_.tolist()))

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
    predataset = pd.read_csv('data/raw_data/small_dataset.csv', sep = ';', index_col=0)
    print('Формирование матрицы TF-IDF')
    tfidf_matrix = get_tfidf(predataset['Required skill'].tolist())

    # Алгоритмы, которые справились с "big_dataset.csv"

    # K-Means, который лучше работает с большими данными (обрабатывает быстрее)
    print('Обработка: MiniBatchKMeans')
    mbkm = mini_batch_k_means(tfidf_matrix)
    mini_batch_k_means_visualization('mini_batch_k_means.jpg', tfidf_matrix, mbkm)
    to_csv('mini_batch_k_means', predataset['Required skill'].tolist(), mbkm)

    print('Обработка: K-Means')
    km = k_means(tfidf_matrix)
    k_means_visualization('k_means.jpg', tfidf_matrix, km)
    to_csv('k_means', predataset['Required skill'].tolist(), km)

    # Алгоритмы, которые не справляются с большим количеством данных, с такими параметрами
    # Возможно нужно настроить параметры или можно уменьшить количество данных (выбирать меньше вакансий по направлению в соответствии с ключевыми словами)
    # Также можно настроить матрицу или использовать другую, например, word2vec

    # Использует много опреативной памяти (>60 гб на данных "big_dataset.csv" и 10-20 гб на данных "middle_dataset.csv")
    # Неправильный результат, долго обрабатывает данные, возможно надо настроить параметры
    print('Обработка: AffinityPropagation')
    ap = affinity_propagation(tfidf_matrix)
    affinity_propagation_visualization('affinity_propagation.jpg', tfidf_matrix, ap)
    to_csv('affinity_propagation', predataset['Required skill'].tolist(), ap)

    # Хорошо обрабатывает небольшое количество данных
    print('Обработка: MeanShift')
    ms = mean_shift(tfidf_matrix)
    mean_shift_visualization('mean_shift.jpg', tfidf_matrix, ms)
    to_csv('mean_shift', predataset['Required skill'].tolist(), ms)

    # Хорошо обрабатывает небольшое количество данных
    print('Обработка: AgglomerativeClustering')
    ac = agglomerative_clustering(tfidf_matrix)
    agglomerative_clustering_visualization('agglomerative_clustering.jpg', tfidf_matrix, ac)
    to_csv('agglomerative_clustering', predataset['Required skill'].tolist(), ac)

    # Много шумов при маленьком количестве данных
    print('Обработка: DBSCAN')
    db = dbscan(tfidf_matrix)
    dbscan_visualization('dbscan.jpg', tfidf_matrix, db)
    to_csv('dbscan', predataset['Required skill'].tolist(), db)

    # Похож на dbscan, много шумов
    print('Обработка: OPTICS')
    op = optics(tfidf_matrix)
    optics_visualization('optics.jpg', tfidf_matrix, op)
    to_csv('optics', predataset['Required skill'].tolist(), op)

    # Хорошо обрабатывает небольшое количество данных
    print('Обработка: Birch')
    br = birch(tfidf_matrix)
    birch_visualization('birch.jpg', tfidf_matrix, br)
    to_csv('birch', predataset['Required skill'].tolist(), br)

    # Обрабатывает небольшое количество данных дольше остальных
    print('Обработка: SpectralClustering')
    sc = spectral_clustering(tfidf_matrix)
    spectral_clustering_visualization('spectral_clustering.jpg', tfidf_matrix, sc)
    to_csv('spectral_clustering', predataset['Required skill'].tolist(), sc)

if __name__ == "__main__":
    clustering() # pass
