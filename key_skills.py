import os
import re
import nltk
import Levenshtein # pip install python-Levenshtein
import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf(skills):
    tfidf = TfidfVectorizer()
    tfidf.fit_transform(skills)
    pd.DataFrame(tfidf.get_feature_names()).to_csv('data/tfidf_sorted_key_skills', sep=';')

def stem_sort(skills):
    sorted_skills = []
    for skill in skills['Required skill']:
        if not skill in nltk.corpus.stopwords.words('russian'):
            sorted_skills.append(nltk.stem.SnowballStemmer('russian', ignore_stopwords=True).stem(skill))
    skills['Required skill'] = sorted_skills

    '''
    sks = skills['Required skill']
    for i in range(len(sks)-1):
        for j in range(len(sks)-i-1):
            if Levenshtein.distance(sks[j], sks[j+1]) < 5:
                sks[j] = sks[j+1]
    '''

    d = {k: v for k, v in sorted(Counter(skills['Required skill']).items(), key=lambda item: item[1], reverse=True)}
    pd.DataFrame(d.keys()).to_csv('data/stem_sorted_key_skills', sep=';')

def sort(skills):
    skills = pd.DataFrame(skills, columns='Required skill')

    stem_sort(skills)
    tfidf(skills['Required skill'])

def main():
    sort([])

if __name__ == "__main__":
    main() # pass
    
