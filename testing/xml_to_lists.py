import xmltodict


def get_standarts():
    with open('data/raw_data/ProfessionalStandarts_566.xml') as fd:
        dataset = xmltodict.parse(fd.read())

    labor_actions = []
    required_skills = []
    necessary_knowledge = []
    possible_job_titles = []
    educational_requirements = []
    for generalized_work_function in \
            dataset['XMLCardInfo']['ProfessionalStandarts']['ProfessionalStandart']['ThirdSection']['WorkFunctions'][
                'GeneralizedWorkFunctions']['GeneralizedWorkFunction']:
        for particular_work_function in generalized_work_function['ParticularWorkFunctions']['ParticularWorkFunction']:
            labor_actions.extend(particular_work_function['LaborActions']['LaborAction'])
            required_skills.extend(particular_work_function['RequiredSkills']['RequiredSkill'])
            necessary_knowledge.extend(particular_work_function['NecessaryKnowledges']['NecessaryKnowledge'])
        possible_job_titles.extend(generalized_work_function['PossibleJobTitles']['PossibleJobTitle'])
        educational_requirements.extend(generalized_work_function['EducationalRequirements']['EducationalRequirement'])

    labor_actions = list(dict.fromkeys(labor_actions))
    required_skills = list(dict.fromkeys(required_skills))
    necessary_knowledge = list(dict.fromkeys(necessary_knowledge))
    possible_job_titles = list(dict.fromkeys(possible_job_titles))
    educational_requirements = list(dict.fromkeys(educational_requirements))

    return required_skills


def to_csv(file_name, data):
    with open('data/{}.csv'.format(file_name), 'w') as f_out:
        f_out.write(';Required skill\n')
        for i in range(len(data)):
            f_out.write('{};{}\n'.format(i, data[i]))
        f_out.close()
