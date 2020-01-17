import cluster as cl
import vacancies as vc

def main():
    specialization_number = input('Введите номер специальности: ')

    arr = vc.get_vacancies_information(specialization_number)

    vc.write_to_csv(vc.get_key_skills(arr), specialization_number + '_key_skills')
    vc.write_to_csv(vc.get_requirements(arr), specialization_number + '_requirements')

    # vc.write_to_csv(cl.clustering(vc.get_requirements(vc.get_vacancies_descriptions(specialization_number))), specialization_number + '_sorted_requirements')

if __name__ == "__main__":
    main()