import time
import data
import processing

def main():
    start = time.time()

    '''
    # Release
    specs = data.get_vacancies(data.get_specializations())
    key_skills_and_requirements = data.get_key_skills(specs) + data.get_requirements(specs)
    matrix = processing.get_tfidf(key_skills_and_requirements)
    clusters = processing.mini_batch_k_means(matrix)
    processing.visualization('mini_batch_k_means.jpg', matrix.toarray(), clusters)
    processing.to_csv('mini_batch_k_means', predataset, clusters)
    '''

    # Debug
    import pandas as pd

    predataset = pd.read_csv('data/raw_data/big_dataset.csv', sep = ';', index_col=0)
    matrix = processing.get_tfidf(predataset['Required skill'].tolist())
    # matrix = processing.get_word2vec(predataset['Required skill'].tolist())

    clusters = processing.dbscan(matrix)
    processing.visualization('dbscan.jpg', matrix, clusters)
    processing.to_csv('dbscan', predataset['Required skill'].tolist(), clusters)

    clusters = processing.mini_batch_k_means(matrix)
    processing.visualization('mini_batch_k_means.jpg', matrix, clusters)
    processing.to_csv('mini_batch_k_means', predataset['Required skill'].tolist(), clusters)

    clusters = processing.agglomerative_clustering(matrix)
    processing.visualization('agglomerative_clustering.jpg', matrix, clusters)
    processing.to_csv('agglomerative_clustering', predataset['Required skill'].tolist(), clusters)

    end = time.time()
    print('Время обработки: {}'.format(end - start))

if __name__ == "__main__":
    main()