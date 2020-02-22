import matplotlib.pyplot as plt


def ward_and_dendrogram(file_name, dataset, matrix):
    from sklearn.metrics.pairwise import cosine_similarity
    dist = 1 - cosine_similarity(matrix)

    from scipy.cluster.hierarchy import ward, dendrogram
    linkage_matrix = ward(dist)

    fig, ax = plt.subplots(figsize=(15, 20))
    ax = dendrogram(linkage_matrix, orientation="right", labels=dataset)

    plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')

    plt.tight_layout()
    plt.savefig('visualization/{}'.format(file_name), dpi=400)
    plt.close()


if __name__ == '__main__':
    pass
