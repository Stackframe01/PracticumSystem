import data
import processing

def main():
    specs = data.get_vacancies(data.get_specializations())

    key_skills_and_requirements = data.get_key_skills(specs) + data.get_requirements(specs)

    tfidf_matrix = processing.get_tfidf(key_skills_and_requirements)

    km = processing.k_means(tfidf_matrix)
    processing.k_means_visualization('k_means.jpg', tfidf_matrix, km)
    processing.to_csv('sorted_k_means', key_skills_and_requirements, km)
    
    db = processing.dbscan(tfidf_matrix)
    processing.dbscan_visualization('dbscan.jpg', tfidf_matrix, db)
    processing.to_csv('sorted_dbscan', key_skills_and_requirements, db)

if __name__ == "__main__":
    main()