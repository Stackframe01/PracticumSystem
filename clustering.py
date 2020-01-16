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

def clustering(reqs): # Лучше, наверное, работать с массивом (чтобы не читать большой файл, все равно массив остается после работы программы), если что можно сделать DataFrame
    predataset = pd.read_csv('data/1.274_requirements.csv', index_col='0', sep = ';')
    predataset.head()
    #predataset['Req'] = predataset['Req'].replace(to_replace=',', value='', regex=True)
    #predataset['Req'] = predataset['Req'].replace(to_replace='.', value='', regex=True)

    nltk.download()

if __name__ == "__main__":
    pass