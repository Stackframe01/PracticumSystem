from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union


@dataclass
class UnitOKVED:
    code_okved: Optional[str]
    name_okved: Optional[str]


@dataclass
class ListOKVED:
    unit_okved: Optional[List[UnitOKVED]]


@dataclass
class ListOKZ:
    unit_okz: Union[List[Dict[str, Optional[str]]], Dict[str, Optional[str]], None]


@dataclass
class EmploymentGroup:
    list_okz: Optional[ListOKZ]
    list_okved: Optional[ListOKVED]


@dataclass
class FirstSection:
    kind_professional_activity: Optional[str]
    code_kind_professional_activity: Optional[str]
    purpose_kind_professional_activity: Optional[str]
    employment_group: Optional[EmploymentGroup]


@dataclass
class OrganizationDevelopers:
    organization_developer: Union[List[str], None, str]


@dataclass
class ResponsibleDeveloper:
    responsible_developer: Optional[str]
    the_position_of_head: Optional[str]
    the_full_name_of_the_head: Optional[str]


@dataclass
class FourthSection:
    responsible_developer: Optional[ResponsibleDeveloper]
    organization_developers: Optional[OrganizationDevelopers]


@dataclass
class EducationalRequirements:
    educational_requirement: Union[List[str], None, str]


class CodeEKS(Enum):
    EMPTY = "-"


@dataclass
class UnitEk:
    code_eks: Optional[CodeEKS]
    name_eks: Optional[str]


@dataclass
class ListEKS:
    unit_eks: Union[List[UnitEk], UnitEk, None]


@dataclass
class UnitOKPDTR:
    code_okpdtr: Optional[int]
    name_okpdtr: Optional[str]


@dataclass
class ListOKPDTR:
    unit_okpdtr: Optional[UnitOKPDTR]


@dataclass
class UnitOKSOElement:
    code_okso: Optional[str]
    name_okso: Optional[str]


@dataclass
class ListOKSO:
    unit_okso: Union[List[UnitOKSOElement], UnitOKSOElement, None]


@dataclass
class OtherCharacteristicPlus:
    list_okz: Optional[ListOKZ]
    list_eks: Optional[ListEKS]
    list_okso: Optional[ListOKSO]
    list_okpdtr: Optional[ListOKPDTR]


@dataclass
class LaborActions:
    labor_action: Union[List[str], None, str]


@dataclass
class NecessaryKnowledges:
    necessary_knowledge: Optional[List[str]]


@dataclass
class RequiredSkills:
    required_skill: Optional[List[str]]


@dataclass
class ParticularWorkFunction:
    sub_qualification: Optional[int]
    other_characteristics: None
    list_footnes: None
    code_tf: Optional[str]
    name_tf: Optional[str]
    labor_actions: Optional[LaborActions]
    required_skills: Optional[RequiredSkills]
    necessary_knowledges: Optional[NecessaryKnowledges]


@dataclass
class ParticularWorkFunctions:
    particular_work_function: Optional[List[ParticularWorkFunction]]


@dataclass
class PossibleJobTitles:
    possible_job_title: Union[List[str], None, str]


@dataclass
class RequirementsWorkExperiences:
    requirements_work_experience: Optional[str]


@dataclass
class GeneralizedWorkFunction:
    level_of_qualification: Optional[int]
    special_conditions_for_admission_to_work: None
    other_characteristics: None
    code_otf: Optional[str]
    name_otf: Optional[str]
    possible_job_titles: Optional[PossibleJobTitles]
    educational_requirements: Optional[EducationalRequirements]
    requirements_work_experiences: Optional[RequirementsWorkExperiences]
    other_characteristic_plus: Optional[OtherCharacteristicPlus]
    particular_work_functions: Optional[ParticularWorkFunctions]


@dataclass
class GeneralizedWorkFunctions:
    generalized_work_function: Optional[List[GeneralizedWorkFunction]]


@dataclass
class WorkFunctions:
    generalized_work_functions: Optional[GeneralizedWorkFunctions]


@dataclass
class ThirdSection:
    work_functions: Optional[WorkFunctions]


@dataclass
class ProfStandart:
    registration_number: Optional[int]
    name_professional_standart: Optional[str]
    order_number: Optional[str]
    date_of_approval: Optional[str]
    first_section: Optional[FirstSection]
    third_section: Optional[ThirdSection]
    fourth_section: Optional[FourthSection]

    class WasNotFound(Exception):
        def __init__(self, code: int, message: str) -> None:
            super().__init__(self, f'Prof standart was not found, code: {code}, message: {message}')


@dataclass
class ProfStandarts:
    professional_standart: Union[List[ProfStandart], ProfStandart]


@dataclass
class XMLCardInfo:
    xmlns_xsi: Optional[str]
    xmlns_xsd: Optional[str]
    professional_standarts: Optional[ProfStandarts]


@dataclass
class ProfStandartsXML:
    xml_card_info: Optional[XMLCardInfo]
