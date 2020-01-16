import vacancies as vc
import clustering as cl

def main():
    specialization_number = input('Введите номер специальности: ')
    vc.write_to_csv(vc.get_requirements(vc.get_vacancies_descriptions(specialization_number)), specialization_number + '_requirements.csv')

    # cl.clustering(vc.get_requirements(vc.get_vacancies_descriptions(specialization_number))

if __name__ == "__main__":
    main()