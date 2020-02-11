import re
import time
import processing
import pandas as pd
import labor_market_needs as lmn
import professional_standarts as ps

def main():
    start = time.time()

    # vacs = lmn.get_vacancies(lmn.get_specializations())
    # predataset = lmn.get_key_skills(vacs) + lmn.get_requirements(vacs)
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