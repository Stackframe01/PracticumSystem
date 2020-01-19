import data
import processing

def main():
    specs = data.get_vacancies(data.get_specializations())

    data.to_csv('key_skills', data.get_key_skills(specs))
    data.to_csv('requirements', data.get_requirements(specs))

    data.to_csv('key_skills_and_requirements', data.get_key_skills(specs) + data.get_requirements(specs))

if __name__ == "__main__":
    main()