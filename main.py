from mysql_database import initializer, exporter
from professional_standarts import downloader, extractor
from professional_standarts.extractor import get_possible_job_titles
from processing import preprocessing, matrices, formation, clustering
from labor_market_needs import downloader as lmn_downloader, extractor as lmn_extractor


def main():
    initializer.initialize_database()

    for generalized_work_function in extractor.get_generalized_work_functions(downloader.get_professional_standards()):
        vacancies = lmn_downloader.get_vacancies(
            preprocessing.get_words(get_possible_job_titles(generalized_work_function)))

        key_skills = lmn_extractor.get_key_skills(vacancies)
        matrix = matrices.get_tfidf(key_skills)
        clusters = clustering.dbscan(matrix)
        key_skills = formation.get_values(formation.get_formatted_data(key_skills, clusters))
        exporter.add_key_skills(generalized_work_function['NameOTF'], key_skills)

        requirements = lmn_extractor.get_requirements(vacancies)
        matrix = matrices.get_tfidf(requirements)
        clusters = clustering.dbscan(matrix)
        requirements = formation.get_values(formation.get_formatted_data(requirements, clusters))
        exporter.add_requirements(generalized_work_function['NameOTF'], requirements)

        professional_standards = []
        for particular_work_function in generalized_work_function['ParticularWorkFunctions']['ParticularWorkFunction']:
            professional_standards.extend(particular_work_function['RequiredSkills']['RequiredSkill'])
        exporter.add_professional_standards(generalized_work_function['NameOTF'], tuple(professional_standards))


if __name__ == '__main__':
    main()
