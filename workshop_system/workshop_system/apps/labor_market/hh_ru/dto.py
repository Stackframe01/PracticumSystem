from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class MetroStation:
    line_id: Optional[int]
    station_id: Optional[str]
    station_name: Optional[str]
    line_name: Optional[str]
    lat: Optional[float]
    lng: Optional[float]


@dataclass
class Address:
    city: Optional[str]
    street: Optional[str]
    building: Optional[str]
    description: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    metro_stations: Optional[List[MetroStation]]


@dataclass
class Area:
    id: Optional[int]
    url: Optional[str]
    name: Optional[str]


@dataclass
class Phone:
    country: Optional[int]
    city: Optional[int]
    comment: Optional[str]
    number: Optional[str]


@dataclass
class Contacts:
    name: Optional[str]
    email: Optional[str]
    phones: Optional[List[Phone]]


@dataclass
class Counters:
    responses: Optional[int]


@dataclass
class Department:
    id: Optional[str]
    name: Optional[str]


@dataclass
class LogoUrls:
    the_90: Optional[str]
    the_240: Optional[str]
    original: Optional[str]


@dataclass
class Employer:
    id: Optional[int]
    logo_urls: Optional[LogoUrls]
    name: Optional[str]
    url: Optional[str]
    alternate_url: Optional[str]
    trusted: Optional[bool]


@dataclass
class InsiderInterview:
    id: Optional[int]
    url: Optional[str]


@dataclass
class Snippet:
    requirement: Optional[str]
    responsibility: Optional[str]


@dataclass
class BillingType:
    id: Optional[str]
    name: Optional[str]


@dataclass
class DriverLicenseType:
    id: Optional[str]


@dataclass
class KeySkill:
    name: Optional[str]


@dataclass
class Specialization:
    profarea_id: Optional[int]
    profarea_name: Optional[str]
    id: Optional[str]
    name: Optional[str]


@dataclass
class Test:
    required: Optional[bool]


@dataclass
class VacancyItem:
    id: Optional[int]
    response_url: Optional[str]
    name: Optional[str]
    insider_interview: Optional[InsiderInterview]
    area: Optional[Area]
    url: Optional[str]
    published_at: Optional[str]
    relations: Optional[List[Any]]
    employer: Optional[Employer]
    contacts: Optional[Contacts]
    response_letter_required: Optional[bool]
    address: Optional[Address]
    sort_point_distance: Optional[float]
    alternate_url: Optional[str]
    apply_alternate_url: Optional[str]
    department: Optional[Department]
    type: Optional[Department]
    has_test: Optional[bool]
    snippet: Optional[Snippet]
    schedule: Optional[Department]
    counters: Optional[Counters]


@dataclass
class VacancyList:
    page: Optional[int]
    per_page: Optional[int]
    items: Optional[List[VacancyItem]]
    clusters: List[Any]
    arguments: List[Any]
    pages: Optional[int]
    found: Optional[int]

    @staticmethod
    def empty():
        return VacancyList(0, 0, [], [], [], 0, 0)


@dataclass
class VacancyFull(VacancyItem):
    description: Optional[str]
    branded_description: Optional[str]
    key_skills: Optional[List[KeySkill]]
    accept_handicapped: Optional[bool]
    accept_kids: Optional[bool]
    experience: Optional[BillingType]
    code: Optional[str]
    employment: Optional[BillingType]
    archived: Optional[bool]
    created_at: Optional[str]
    test: Optional[Test]
    specializations: Optional[List[Specialization]]
    billing_type: Optional[BillingType]
    allow_messages: Optional[bool]
    premium: Optional[bool]
    driver_license_types: Optional[List[DriverLicenseType]]
    accept_incomplete_resumes: Optional[bool]
    working_days: Optional[List[BillingType]]
    working_time_intervals: Optional[List[BillingType]]
    working_time_modes: Optional[List[BillingType]]
    accept_temporary: Optional[bool]

    class WasNotFound(Exception):
        def __init__(self, code: int, message: str) -> None:
            super().__init__(self, f'Vacancy was not found, code: {code}, message: {message}')
