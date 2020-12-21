from sklearn.cluster import MiniBatchKMeans, KMeans, AffinityPropagation, MeanShift, SpectralClustering, \
    AgglomerativeClustering, DBSCAN, OPTICS, Birch, SpectralBiclustering, SpectralCoclustering, FeatureAgglomeration


def mini_batch_k_means(tfidf_matrix, n_clusters=100):
    return MiniBatchKMeans(n_clusters=n_clusters).fit(tfidf_matrix)


def k_means(tfidf_matrix, n_clusters=100):
    return KMeans(n_clusters=n_clusters).fit(tfidf_matrix)


def affinity_propagation(tfidf_matrix, damping=0.5, max_iter=200, convergence_iter=15):
    return AffinityPropagation(damping=damping, max_iter=max_iter, convergence_iter=convergence_iter).fit(tfidf_matrix)


def mean_shift(tfidf_matrix, bandwidth=None):
    return MeanShift(bandwidth=bandwidth).fit(tfidf_matrix)


def spectral_clustering(tfidf_matrix, n_clusters=100):
    return SpectralClustering(n_clusters=n_clusters).fit(tfidf_matrix)


def agglomerative_clustering(tfidf_matrix, n_clusters=100):
    return AgglomerativeClustering(n_clusters=n_clusters).fit(tfidf_matrix)


def dbscan(tfidf_matrix, eps=0.001, min_samples=2, n_jobs=-1, leaf_size=100):
    return DBSCAN(eps=eps, min_samples=min_samples, n_jobs=n_jobs, leaf_size=leaf_size).fit(tfidf_matrix)


def optics(tfidf_matrix, min_samples=5):
    return OPTICS(min_samples=min_samples).fit(tfidf_matrix)


def birch(tfidf_matrix, n_clusters=100, threshold=0.01):
    return Birch(n_clusters=n_clusters, threshold=threshold).fit(tfidf_matrix)


def spectral_biclustering(tfidf_matrix, n_clusters=100):
    return SpectralBiclustering(n_clusters=n_clusters).fit(tfidf_matrix)


def spectral_coclustering(tfidf_matrix, n_clusters=100):
    return SpectralCoclustering(n_clusters=n_clusters).fit(tfidf_matrix)


def feature_agglomeration(tfidf_matrix, n_clusters=100):
    return FeatureAgglomeration(n_clusters=n_clusters).fit(tfidf_matrix)


if __name__ == '__main__':
    pass
