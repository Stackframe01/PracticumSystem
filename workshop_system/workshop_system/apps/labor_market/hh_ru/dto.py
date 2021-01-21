from dataclasses import dataclass
from typing import List, Any


@dataclass
class MetroStation:
    station_id: str
    station_name: str
    line_id: int
    line_name: str
    lat: float
    lng: float


@dataclass
class Address:
    city: str
    street: str
    building: str
    description: str
    lat: float
    lng: float
    metro_stations: List[MetroStation]


@dataclass
class Area:
    url: str
    id: int
    name: str


@dataclass
class BillingType:
    id: str
    name: str


@dataclass
class Phone:
    country: int
    city: int
    number: str
    comment: None


@dataclass
class Contacts:
    name: str
    email: str
    phones: List[Phone]


@dataclass
class DriverLicenseType:
    id: str


@dataclass
class LogoUrls:
    the_90: str
    the_240: str
    original: str


@dataclass
class Employer:
    logo_urls: LogoUrls
    name: str
    url: str
    alternate_url: str
    id: int
    trusted: bool
    blacklisted: bool


@dataclass
class InsiderInterview:
    id: int
    url: str


@dataclass
class KeySkill:
    name: str


@dataclass
class Salary:
    to: None
    salary_from: int
    currency: str
    gross: bool


@dataclass
class Specialization:
    profarea_id: int
    profarea_name: str
    id: str
    name: str


@dataclass
class Test:
    required: bool


@dataclass
class Counters:
    responses: int


@dataclass
class Department:
    id: str
    name: str


@dataclass
class Snippet:
    requirement: str
    responsibility: str


@dataclass
class VacancyItem:
    salary: Salary
    name: str
    insider_interview: InsiderInterview
    area: Area
    url: str
    published_at: str
    relations: List[Any]
    employer: Employer
    contacts: Contacts
    response_letter_required: bool
    address: Address
    sort_point_distance: float
    alternate_url: str
    apply_alternate_url: str
    department: Department
    type: Department
    id: int
    has_test: bool
    response_url: None
    snippet: Snippet
    schedule: Department
    counters: Counters


@dataclass
class VacancyList:
    per_page: int
    items: List[VacancyItem]
    page: int
    pages: int
    found: int
    clusters: None
    arguments: None


@dataclass
class VacancyFull(VacancyItem):
    description: str
    branded_description: str
    key_skills: List[KeySkill]
    accept_handicapped: bool
    accept_kids: bool
    experience: BillingType
    code: str
    employment: BillingType
    archived: bool
    created_at: str
    test: Test
    specializations: List[Specialization]
    billing_type: BillingType
    allow_messages: bool
    premium: bool
    driver_license_types: List[DriverLicenseType]
    accept_incomplete_resumes: bool
    working_days: List[BillingType]
    working_time_intervals: List[BillingType]
    working_time_modes: List[BillingType]
    accept_temporary: bool
