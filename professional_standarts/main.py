import re
import time
import data
import processing

def main():
    start = time.time()

    dataset = data.get_standarts()

    matrix = processing.get_tfidf(dataset)
    clusters = processing.dbscan(matrix)
    processing.to_csv("processed_data.csv", dataset, clusters)

    print('Время обработки: {}'.format(time.time() - start))

if __name__ == "__main__":
    main()