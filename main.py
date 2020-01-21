import data
import processing

def main():
    specs = data.get_vacancies(data.get_specializations())

    key_skills_and_requirements = data.get_key_skills(specs) + data.get_requirements(specs)

    tfidf_matrix = processing.get_tfidf(key_skills_and_requirements)

    clusters = processing.mini_batch_k_means(tfidf_matrix) # Выбрать алгоритм кластеризации, пока что с большими данными лучше всего справляется MiniBatchKMeans
    processing.mini_batch_k_means_visualization('mini_batch_k_means.jpg', tfidf_matrix, clusters)
    processing.to_csv('mini_batch_k_means', key_skills_and_requirements, clusters)

if __name__ == "__main__":
    main()