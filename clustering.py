import os
import re
import nltk
import mpld3
import codecs
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import feature_extraction
#
#
#
predataset = pd.read_csv('data/1.274_requirements.csv', index_col='0', sep = ';')
#print(predataset['Text'])
#predataset[] = predataset.replace(to_replace=',', value='', regex=True)
#print(predataset.head())
#predataset['Req'] = predataset['Req'].replace(to_replace='.', value='', regex=True)
'''
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")

def token_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[а-яА-Я]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def token_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[а-яА-Я]', token):
            filtered_tokens.append(token)
    return filtered_tokens

#Создаем словари (массивы) из полученных основ
totalvocab_stem = []
totalvocab_token = []
for i in predataset['Req']:
    allwords_stemmed = token_and_stem(i)
    #print(allwords_stemmed)
    totalvocab_stem.extend(allwords_stemmed)
    
    allwords_tokenized = token_only(i)
    totalvocab_token.extend(allwords_tokenized)

#Кластеризацияч полученных данных
num_clusters = 5

# Метод к-средних - KMeans
from sklearn.cluster import KMeans

km = KMeans(n_clusters=num_clusters)
get_ipython().magic('time km.fit(tfidf_matrix)')
idx = km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

print(clusters)
print (km.labels_)

# DBSCAN
from sklearn.cluster import DBSCAN
get_ipython().magic('time db = DBSCAN(eps=0.3, min_samples=10).fit(tfidf_matrix)')
labels = db.labels_
labels.shape
print(labels)

#k-means
clusterkm = km.labels_.tolist()

#dbscan
clusters3 = labels
frame = pd.DataFrame(titles, index = [clusterkm])

#k-means
out = { 'title': titles, 'cluster': clusterkm }
frame1 = pd.DataFrame(out, index = [clusterkm], columns = ['title', 'cluster'])
frame1['cluster'].value_counts()

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)
dist.shape

# СОКРАЩЕНИЕ РАЗМЕРНОСТИ ДАННЫХ PCA

from sklearn.decomposition import IncrementalPCA
icpa = IncrementalPCA(n_components=2, batch_size=16)
get_ipython().magic('time icpa.fit(dist) #demo =')
get_ipython().magic('time demo2 = icpa.transform(dist)')
xs, ys = demo2[:, 0], demo2[:, 1]

# PCA 3D
from sklearn.decomposition import IncrementalPCA
icpa = IncrementalPCA(n_components=3, batch_size=16)
get_ipython().magic('time icpa.fit(dist) #demo =')
get_ipython().magic('time ddd = icpa.transform(dist)')
xs, ys, zs = ddd[:, 0], ddd[:, 1], ddd[:, 2]
'''
'''
ПОДХОД К ВИЗУАЛИЗАЦИИ
from matplotlib import rc
#включаем русские символы на графике
font = {'family' : 'Verdana'}#, 'weigth': 'normal'}
rc('font', **font)

#цвета для кластеров
import random
def generate_colors(n):
    color_list = []
    for c in range(0,n):
        r = lambda: random.randint(0,255)
        color_list.append( '#%02X%02X%02X' % (r(),r(),r()) )
    return color_list
'''
def clustering(reqs): # Лучше, наверное, работать с массивом (чтобы не читать большой файл, все равно массив остается после работы программы), если что можно сделать DataFrame
    predataset = pd.read_csv('data/1.274_requirements.csv', index_col='0', sep = ';')
    predataset.head()
    #predataset['Req'] = predataset['Req'].replace(to_replace=',', value='', regex=True)
    #predataset['Req'] = predataset['Req'].replace(to_replace='.', value='', regex=True)

    nltk.download()

if __name__ == "__main__":
    pass
