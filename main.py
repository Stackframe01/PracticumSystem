from mysql_database import initializer, exporter
from professional_standards import downloader, extractor
from processing import preprocessing, matrices, formation, clustering
from labor_market_needs import downloader as lmn_downloader, extractor as lmn_extractor


def main():
    initializer.initialize_database()
    downloader.clear_downloads()
    # downloader.download_professional_standards_by_id('50443')
    downloader.download_professional_standards_by_name('Системный программист')

    for professional_standart in extractor.get_professional_standards(
            downloader.get_latest_downloaded_professional_standards()):
        for generalized_work_function in extractor.get_generalized_work_functions(professional_standart):
            vacancies = lmn_downloader.get_vacancies(
                preprocessing.get_words(extractor.get_possible_job_titles(generalized_work_function)))

            key_skills = lmn_extractor.get_key_skills(vacancies)
            if len(key_skills) != 0:
                matrix = matrices.get_tfidf(key_skills)
                clusters = clustering.dbscan(matrix)
                key_skills = formation.get_values(formation.get_formatted_data(key_skills, clusters))
                exporter.add_key_skills(professional_standart['NameProfessionalStandart'],
                                        generalized_work_function['NameOTF'], key_skills)

            requirements = lmn_extractor.get_requirements(vacancies)
            if len(requirements) != 0:
                matrix = matrices.get_tfidf(requirements)
                clusters = clustering.dbscan(matrix)
                requirements = formation.get_values(formation.get_formatted_data(requirements, clusters))
                exporter.add_requirements(professional_standart['NameProfessionalStandart'],
                                          generalized_work_function['NameOTF'], requirements)

            professional_standards = []
            for particular_work_function in generalized_work_function['ParticularWorkFunctions'][
                'ParticularWorkFunction']:
                professional_standards.extend(particular_work_function['RequiredSkills']['RequiredSkill'])
            if len(professional_standards) != 0:
                exporter.add_professional_standards(professional_standart['NameProfessionalStandart'],
                                                    generalized_work_function['NameOTF'], tuple(professional_standards))


if __name__ == '__main__':
    main()
