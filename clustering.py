import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
import matplotlib.pyplot as plt
import matplotlib as mpl

predataset = pd.read_csv('data/1.274_requirements.csv', index_col='0', sep = ';')
predataset.head()
#predataset['Req'] = predataset['Req'].replace(to_replace=',', value='', regex=True)
#predataset['Req'] = predataset['Req'].replace(to_replace='.', value='', regex=True)

nltk.download()

