import cluster
import vacancies

def main():
    links = vacancies.get_vacancies(vacancies.get_specializations())

    vacancies.to_csv(vacancies.get_key_skills(links), 'key_skills')
    vacancies.to_csv(vacancies.get_requirements(links), 'requirements')

if __name__ == "__main__":
    main()