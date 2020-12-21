import re
from mysql_database import importer


def get_requirements(vacancies):
    regex_start = '|'.join(set(importer.get_description_regex_start()))
    regex_end = '|'.join(set(importer.get_description_regex_end()))

    reqs = []
    for i in vacancies:
        for j in re.findall('(?:{}).*?(?:{})'.format(regex_start, regex_end), i['description'],
                            re.IGNORECASE):
            for k in re.findall(r'<li>.*?</li>', j):
                reqs.append(re.sub(r'(?:^\s+|\.|;|,)', '', re.sub(r'<.*?>', '', str(k))).lower())

    return [i for i in reqs if i != '']


def get_key_skills(vacancies):
    skills = []
    for i in vacancies:
        for j in i['key_skills']:
            skills.append(j['name'])

    for i in skills:
        sequence = re.findall(r'.*?[.;,]', i)
        if sequence:
            skills.remove(i)
            skills.extend(sequence)

    return [i for i in [re.sub(r'(?:^\s+|\.|;|,)', '', i).lower() for i in skills] if i != '']


if __name__ == '__main__':
    pass
