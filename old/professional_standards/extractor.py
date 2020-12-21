import xmltodict


def get_professional_standards(professional_standards):
    professional_standards = xmltodict.parse(professional_standards)['XMLCardInfo']['ProfessionalStandarts']['ProfessionalStandart']
    if len(professional_standards) > 10:
        print('File is too big. Comment this statement if you want to process it anyway')
        return None
    try:
        professional_standards["ThirdSection"]
        return [professional_standards]
    except:
        return professional_standards


def get_generalized_work_functions(professional_standard):
    return professional_standard["ThirdSection"]['WorkFunctions']['GeneralizedWorkFunctions']['GeneralizedWorkFunction']


def get_possible_job_titles(work_function):
    return work_function['PossibleJobTitles']['PossibleJobTitle']


if __name__ == '__main__':
    pass
