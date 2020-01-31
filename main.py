import re
import time
import data
import processing
import pandas as pd

def main():
    start = time.time()

    # vacs = data.get_vacancies(data.get_specializations())
    # predataset = data.get_key_skills(vacs) + data.get_requirements(vacs)
    predataset = pd.read_csv('data/raw_data/dataset.csv', sep = ';', index_col=0)['Required skill'].tolist()
    matrix = processing.get_tfidf(predataset)
    # matrix = processing.get_word2vec(predataset['Required skill'].tolist())

    print('Here')
    clusters = processing.dbscan(matrix)
    file_name = re.sub(r'\((?:.|\n)*', '', str(clusters))
    processing.visualization('{}.jpg'.format(file_name), matrix, clusters)
    processing.to_csv(file_name, predataset, clusters)

    print('Время обработки: {}'.format(time.time() - start))

if __name__ == "__main__":
    main()