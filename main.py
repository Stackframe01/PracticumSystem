import cluster as cl
import vacancies as vc

def main():
    specialization_number = input('Введите номер специальности: ')
    vc.write_to_csv(vc.get_requirements(vc.get_vacancies_descriptions(specialization_number)), specialization_number + '_requirements')

    # vc.write_to_csv(cl.clustering(vc.get_requirements(vc.get_vacancies_descriptions(specialization_number))), specialization_number + '_sorted_requirements')

if __name__ == "__main__":
    main()