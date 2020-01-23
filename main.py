import data
import processing

def main():
    specs = data.get_vacancies(data.get_specializations())
    predataset = data.get_key_skills(specs) + data.get_requirements(specs)
    matrix = processing.get_tfidf(predataset)
    clusters = processing.dbscan(matrix)
    processing.to_csv('required_skills', predataset, clusters)

if __name__ == "__main__":
    main()