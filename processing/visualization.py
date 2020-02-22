import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def visualization(file_name, matrix, clusters):
    X = PCA(n_components=2).fit_transform(matrix)
    plt.scatter(X[:, 0], X[:, 1], c=clusters.fit_predict(X))
    plt.savefig('visualization/{}'.format(file_name), dpi=200)
    plt.close()


if __name__ == '__main__':
    pass
