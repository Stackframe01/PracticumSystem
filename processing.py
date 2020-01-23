import re
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans, KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, DBSCAN, OPTICS, Birch

# МАТРИЦЫ

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

    return tfidf_matrix.toarray()

def get_word2vec(dataset):
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

    preprocessed = []
    for i in dataset:
        temp = token_and_stem(i)
        if temp not in stopwords:
            preprocessed.append(temp)
    
    model = Word2Vec(preprocessed)
    return model[model.wv.vocab]

# АЛГОРИТМЫ

def mini_batch_k_means(tfidf_matrix, n_clusters=100):
    return MiniBatchKMeans(n_clusters=n_clusters).fit(tfidf_matrix)

def k_means(tfidf_matrix, n_clusters=100):
    return KMeans(n_clusters=n_clusters).fit(tfidf_matrix)

def affinity_propagation(tfidf_matrix, damping=0.5, max_iter=200, convergence_iter=15):
    return AffinityPropagation(damping=damping, max_iter=max_iter, convergence_iter=convergence_iter).fit(tfidf_matrix)

def mean_shift(tfidf_matrix, bandwidth=None):
    return MeanShift(bandwidth=bandwidth).fit(tfidf_matrix)

def spectral_clustering(tfidf_matrix, n_clusters=100):
    return SpectralClustering(n_clusters=n_clusters).fit(tfidf_matrix)

def agglomerative_clustering(tfidf_matrix, n_clusters=100):
    return AgglomerativeClustering(n_clusters=n_clusters).fit(tfidf_matrix)

def dbscan(tfidf_matrix, eps=0.001, min_samples=2):
    return DBSCAN(eps=eps, min_samples=min_samples).fit(tfidf_matrix)

def optics(tfidf_matrix, min_samples=5):
    return OPTICS(min_samples=min_samples).fit(tfidf_matrix)

def birch(tfidf_matrix, n_clusters=100, threshold=0.01):
    return Birch(n_clusters=n_clusters, threshold=threshold).fit(tfidf_matrix)

def ward_and_dendrogram(file_name, dataset, matrix):
    from sklearn.metrics.pairwise import cosine_similarity
    dist = 1 - cosine_similarity(matrix)

    from scipy.cluster.hierarchy import ward, dendrogram
    linkage_matrix = ward(dist)

    fig, ax = plt.subplots(figsize=(15, 20))
    ax = dendrogram(linkage_matrix, orientation="right", labels=dataset)

    plt.tick_params(axis= 'x', which='both', bottom='off', top='off', labelbottom='off')

    plt.tight_layout()
    plt.savefig('visualization/{}'.format(file_name), dpi=400)
    plt.close()

# ВИЗУАЛИЗАЦИЯ

def visualization(file_name, matrix, clusters):
    X = PCA(n_components=2).fit_transform(matrix)
    plt.scatter(X[:,0], X[:,1],c=clusters.fit_predict(X))
    plt.savefig('visualization/{}'.format(file_name), dpi=200)
    plt.close()

def to_csv(file_name, dataset, cluster):
    out = dict(zip(dataset, cluster.labels_.tolist()))

    new_out = {}
    for key, value in out.items():
        if value not in new_out:
            new_out[value] = [key]
        else:
            new_out[value].append(key)

    new_out = {k: v for k, v in sorted(new_out.items(), key=lambda item: len(item[1]), reverse=True)}
    
    framedb = pd.DataFrame({'Skills': list(new_out.values()), 'Cluster': list(new_out.keys())}, columns = ['Skills', 'Cluster'])
    framedb.to_csv('data/processed_data/{}.csv'.format(file_name), sep=';')

if __name__ == "__main__":
    pass
