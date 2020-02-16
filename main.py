import ps
import lmn
import export
import processing

def main():
    for generalized_work_function in ps.get_generalized_work_functions():
        specializations_ids = lmn.get_specializations_ids(processing.get_words(ps.get_possible_job_titles(generalized_work_function)))
        vacancies = lmn.get_vacancies(specializations_ids)
        key_skills_and_requirements = lmn.get_key_skills(vacancies) + lmn.get_requirements(vacancies)

        matrix = processing.get_tfidf(key_skills_and_requirements)
        clusters = processing.dbscan(matrix)

        # Вставка в mysql по имени generalized_work_function['NameOTF']

if __name__ == "__main__":
    main()