import xmltodict

def get_generalized_work_functions():
    with open('data/raw_data/ProfessionalStandarts_566.xml') as fd:
        dataset = xmltodict.parse(fd.read())

    return dataset['XMLCardInfo']['ProfessionalStandarts']['ProfessionalStandart']['ThirdSection']['WorkFunctions']['GeneralizedWorkFunctions']['GeneralizedWorkFunction']

def get_possible_job_titles(generalized_work_function):
    return generalized_work_function['PossibleJobTitles']['PossibleJobTitle']


if __name__ == "__main__":
    pass