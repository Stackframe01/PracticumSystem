import xmltodict


def get_generalized_work_functions(professional_standards):
    return xmltodict.parse(professional_standards)['XMLCardInfo']['ProfessionalStandarts']['ProfessionalStandart'][
        "ThirdSection"]['WorkFunctions']['GeneralizedWorkFunctions']['GeneralizedWorkFunction']


def get_possible_job_titles(work_function):
    return work_function['PossibleJobTitles']['PossibleJobTitle']


if __name__ == '__main__':
    pass
