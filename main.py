import ps
import lmn
import export
import processing

def main():
    for generalized_work_function in ps.get_generalized_work_functions():
        vacancies = lmn.get_vacancies(processing.get_words(ps.get_possible_job_titles(generalized_work_function)))

        '''
        # Можно сохранять key_skills с обработкой на повтрения
        key_skills = list(set(lmn.get_key_skills(vacancies)))
        # А requirements обрабатывать с посощью кластеризации отдельно
        '''

        # Обработка и кластеризация всего сразу
        key_skills_and_requirements = lmn.get_key_skills(vacancies) + lmn.get_requirements(vacancies)
        matrix = processing.get_tfidf(key_skills_and_requirements)
        clusters = processing.dbscan(matrix)
        processing.to_csv('dbscan', key_skills_and_requirements, clusters)

        # Вставка в mysql для каждой рабочей функции

if __name__ == "__main__":
    main()