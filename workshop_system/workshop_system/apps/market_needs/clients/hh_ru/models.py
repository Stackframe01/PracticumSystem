from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class MetroStation:
    station_id: str
    station_name: str
    line_id: int
    line_name: str
    lat: float
    lng: float

    def __init__(self, station_id: str, station_name: str, line_id: int, line_name: str, lat: float,
                 lng: float) -> None:
        self.station_id = station_id
        self.station_name = station_name
        self.line_id = line_id
        self.line_name = line_name
        self.lat = lat
        self.lng = lng

    @staticmethod
    def from_dict(obj: Any) -> 'MetroStation':
        assert isinstance(obj, dict)
        station_id = from_str(obj.get("station_id"))
        station_name = from_str(obj.get("station_name"))
        line_id = int(from_str(obj.get("line_id")))
        line_name = from_str(obj.get("line_name"))
        lat = from_float(obj.get("lat"))
        lng = from_float(obj.get("lng"))
        return MetroStation(station_id, station_name, line_id, line_name, lat, lng)

    def to_dict(self) -> dict:
        result: dict = {}
        result["station_id"] = from_str(self.station_id)
        result["station_name"] = from_str(self.station_name)
        result["line_id"] = from_str(str(self.line_id))
        result["line_name"] = from_str(self.line_name)
        result["lat"] = to_float(self.lat)
        result["lng"] = to_float(self.lng)
        return result


class Address:
    city: str
    street: str
    building: str
    description: str
    lat: float
    lng: float
    metro_stations: List[MetroStation]

    def __init__(self, city: str, street: str, building: str, description: str, lat: float, lng: float,
                 metro_stations: List[MetroStation]) -> None:
        self.city = city
        self.street = street
        self.building = building
        self.description = description
        self.lat = lat
        self.lng = lng
        self.metro_stations = metro_stations

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        city = from_str(obj.get("city"))
        street = from_str(obj.get("street"))
        building = from_str(obj.get("building"))
        description = from_str(obj.get("description"))
        lat = from_float(obj.get("lat"))
        lng = from_float(obj.get("lng"))
        metro_stations = from_list(MetroStation.from_dict, obj.get("metro_stations"))
        return Address(city, street, building, description, lat, lng, metro_stations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city"] = from_str(self.city)
        result["street"] = from_str(self.street)
        result["building"] = from_str(self.building)
        result["description"] = from_str(self.description)
        result["lat"] = to_float(self.lat)
        result["lng"] = to_float(self.lng)
        result["metro_stations"] = from_list(lambda x: to_class(MetroStation, x), self.metro_stations)
        return result


class Area:
    url: str
    id: int
    name: str

    def __init__(self, url: str, id: int, name: str) -> None:
        self.url = url
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Area':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        id = int(from_str(obj.get("id")))
        name = from_str(obj.get("name"))
        return Area(url, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["id"] = from_str(str(self.id))
        result["name"] = from_str(self.name)
        return result


class BillingType:
    id: str
    name: str

    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'BillingType':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        return BillingType(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        return result


class Phone:
    country: int
    city: int
    number: str
    comment: None

    def __init__(self, country: int, city: int, number: str, comment: None) -> None:
        self.country = country
        self.city = city
        self.number = number
        self.comment = comment

    @staticmethod
    def from_dict(obj: Any) -> 'Phone':
        assert isinstance(obj, dict)
        country = int(from_str(obj.get("country")))
        city = int(from_str(obj.get("city")))
        number = from_str(obj.get("number"))
        comment = from_none(obj.get("comment"))
        return Phone(country, city, number, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["country"] = from_str(str(self.country))
        result["city"] = from_str(str(self.city))
        result["number"] = from_str(self.number)
        result["comment"] = from_none(self.comment)
        return result


class Contacts:
    name: str
    email: str
    phones: List[Phone]

    def __init__(self, name: str, email: str, phones: List[Phone]) -> None:
        self.name = name
        self.email = email
        self.phones = phones

    @staticmethod
    def from_dict(obj: Any) -> 'Contacts':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        email = from_str(obj.get("email"))
        phones = from_list(Phone.from_dict, obj.get("phones"))
        return Contacts(name, email, phones)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["email"] = from_str(self.email)
        result["phones"] = from_list(lambda x: to_class(Phone, x), self.phones)
        return result


class DriverLicenseType:
    id: str

    def __init__(self, id: str) -> None:
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'DriverLicenseType':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        return DriverLicenseType(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        return result


class LogoUrls:
    the_90: str
    the_240: str
    original: str

    def __init__(self, the_90: str, the_240: str, original: str) -> None:
        self.the_90 = the_90
        self.the_240 = the_240
        self.original = original

    @staticmethod
    def from_dict(obj: Any) -> 'LogoUrls':
        assert isinstance(obj, dict)
        the_90 = from_str(obj.get("90"))
        the_240 = from_str(obj.get("240"))
        original = from_str(obj.get("original"))
        return LogoUrls(the_90, the_240, original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["90"] = from_str(self.the_90)
        result["240"] = from_str(self.the_240)
        result["original"] = from_str(self.original)
        return result


class Employer:
    logo_urls: LogoUrls
    name: str
    url: str
    alternate_url: str
    id: int
    trusted: bool
    blacklisted: bool

    def __init__(self, logo_urls: LogoUrls, name: str, url: str, alternate_url: str, id: int, trusted: bool,
                 blacklisted: bool) -> None:
        self.logo_urls = logo_urls
        self.name = name
        self.url = url
        self.alternate_url = alternate_url
        self.id = id
        self.trusted = trusted
        self.blacklisted = blacklisted

    @staticmethod
    def from_dict(obj: Any) -> 'Employer':
        assert isinstance(obj, dict)
        logo_urls = LogoUrls.from_dict(obj.get("logo_urls"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        alternate_url = from_str(obj.get("alternate_url"))
        id = int(from_str(obj.get("id")))
        trusted = from_bool(obj.get("trusted"))
        blacklisted = from_bool(obj.get("blacklisted"))
        return Employer(logo_urls, name, url, alternate_url, id, trusted, blacklisted)

    def to_dict(self) -> dict:
        result: dict = {}
        result["logo_urls"] = to_class(LogoUrls, self.logo_urls)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        result["alternate_url"] = from_str(self.alternate_url)
        result["id"] = from_str(str(self.id))
        result["trusted"] = from_bool(self.trusted)
        result["blacklisted"] = from_bool(self.blacklisted)
        return result


class InsiderInterview:
    id: int
    url: str

    def __init__(self, id: int, url: str) -> None:
        self.id = id
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'InsiderInterview':
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("id")))
        url = from_str(obj.get("url"))
        return InsiderInterview(id, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(str(self.id))
        result["url"] = from_str(self.url)
        return result


class KeySkill:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'KeySkill':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        return KeySkill(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        return result


class Salary:
    to: None
    salary_from: int
    currency: str
    gross: bool

    def __init__(self, to: None, salary_from: int, currency: str, gross: bool) -> None:
        self.to = to
        self.salary_from = salary_from
        self.currency = currency
        self.gross = gross

    @staticmethod
    def from_dict(obj: Any) -> 'Salary':
        assert isinstance(obj, dict)
        to = from_none(obj.get("to"))
        salary_from = from_int(obj.get("from"))
        currency = from_str(obj.get("currency"))
        gross = from_bool(obj.get("gross"))
        return Salary(to, salary_from, currency, gross)

    def to_dict(self) -> dict:
        result: dict = {}
        result["to"] = from_none(self.to)
        result["from"] = from_int(self.salary_from)
        result["currency"] = from_str(self.currency)
        result["gross"] = from_bool(self.gross)
        return result


class Specialization:
    profarea_id: int
    profarea_name: str
    id: str
    name: str

    def __init__(self, profarea_id: int, profarea_name: str, id: str, name: str) -> None:
        self.profarea_id = profarea_id
        self.profarea_name = profarea_name
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Specialization':
        assert isinstance(obj, dict)
        profarea_id = int(from_str(obj.get("profarea_id")))
        profarea_name = from_str(obj.get("profarea_name"))
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        return Specialization(profarea_id, profarea_name, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["profarea_id"] = from_str(str(self.profarea_id))
        result["profarea_name"] = from_str(self.profarea_name)
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        return result


class Test:
    required: bool

    def __init__(self, required: bool) -> None:
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'Test':
        assert isinstance(obj, dict)
        required = from_bool(obj.get("required"))
        return Test(required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["required"] = from_bool(self.required)
        return result


class Vacancy:
    id: int
    description: str
    branded_description: str
    key_skills: List[KeySkill]
    schedule: BillingType
    accept_handicapped: bool
    accept_kids: bool
    experience: BillingType
    address: Address
    alternate_url: str
    apply_alternate_url: str
    code: str
    department: BillingType
    employment: BillingType
    salary: Salary
    archived: bool
    name: str
    insider_interview: InsiderInterview
    area: Area
    created_at: str
    published_at: str
    employer: Employer
    response_letter_required: bool
    type: BillingType
    has_test: bool
    response_url: None
    test: Test
    specializations: List[Specialization]
    contacts: Contacts
    billing_type: BillingType
    allow_messages: bool
    premium: bool
    driver_license_types: List[DriverLicenseType]
    accept_incomplete_resumes: bool
    working_days: List[BillingType]
    working_time_intervals: List[BillingType]
    working_time_modes: List[BillingType]
    accept_temporary: bool

    def __init__(self, id: int, description: str, branded_description: str, key_skills: List[KeySkill],
                 schedule: BillingType, accept_handicapped: bool, accept_kids: bool, experience: BillingType,
                 address: Address, alternate_url: str, apply_alternate_url: str, code: str, department: BillingType,
                 employment: BillingType, salary: Salary, archived: bool, name: str,
                 insider_interview: InsiderInterview, area: Area, created_at: str, published_at: str,
                 employer: Employer, response_letter_required: bool, type: BillingType, has_test: bool,
                 response_url: None, test: Test, specializations: List[Specialization], contacts: Contacts,
                 billing_type: BillingType, allow_messages: bool, premium: bool,
                 driver_license_types: List[DriverLicenseType], accept_incomplete_resumes: bool,
                 working_days: List[BillingType], working_time_intervals: List[BillingType],
                 working_time_modes: List[BillingType], accept_temporary: bool) -> None:
        self.id = id
        self.description = description
        self.branded_description = branded_description
        self.key_skills = key_skills
        self.schedule = schedule
        self.accept_handicapped = accept_handicapped
        self.accept_kids = accept_kids
        self.experience = experience
        self.address = address
        self.alternate_url = alternate_url
        self.apply_alternate_url = apply_alternate_url
        self.code = code
        self.department = department
        self.employment = employment
        self.salary = salary
        self.archived = archived
        self.name = name
        self.insider_interview = insider_interview
        self.area = area
        self.created_at = created_at
        self.published_at = published_at
        self.employer = employer
        self.response_letter_required = response_letter_required
        self.type = type
        self.has_test = has_test
        self.response_url = response_url
        self.test = test
        self.specializations = specializations
        self.contacts = contacts
        self.billing_type = billing_type
        self.allow_messages = allow_messages
        self.premium = premium
        self.driver_license_types = driver_license_types
        self.accept_incomplete_resumes = accept_incomplete_resumes
        self.working_days = working_days
        self.working_time_intervals = working_time_intervals
        self.working_time_modes = working_time_modes
        self.accept_temporary = accept_temporary

    @staticmethod
    def from_dict(obj: Any) -> 'Vacancy':
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("id")))
        description = from_str(obj.get("description"))
        branded_description = from_str(obj.get("branded_description"))
        key_skills = from_list(KeySkill.from_dict, obj.get("key_skills"))
        schedule = BillingType.from_dict(obj.get("schedule"))
        accept_handicapped = from_bool(obj.get("accept_handicapped"))
        accept_kids = from_bool(obj.get("accept_kids"))
        experience = BillingType.from_dict(obj.get("experience"))
        address = Address.from_dict(obj.get("address"))
        alternate_url = from_str(obj.get("alternate_url"))
        apply_alternate_url = from_str(obj.get("apply_alternate_url"))
        code = from_str(obj.get("code"))
        department = BillingType.from_dict(obj.get("department"))
        employment = BillingType.from_dict(obj.get("employment"))
        salary = Salary.from_dict(obj.get("salary"))
        archived = from_bool(obj.get("archived"))
        name = from_str(obj.get("name"))
        insider_interview = InsiderInterview.from_dict(obj.get("insider_interview"))
        area = Area.from_dict(obj.get("area"))
        created_at = from_str(obj.get("created_at"))
        published_at = from_str(obj.get("published_at"))
        employer = Employer.from_dict(obj.get("employer"))
        response_letter_required = from_bool(obj.get("response_letter_required"))
        type = BillingType.from_dict(obj.get("type"))
        has_test = from_bool(obj.get("has_test"))
        response_url = from_none(obj.get("response_url"))
        test = Test.from_dict(obj.get("test"))
        specializations = from_list(Specialization.from_dict, obj.get("specializations"))
        contacts = Contacts.from_dict(obj.get("contacts"))
        billing_type = BillingType.from_dict(obj.get("billing_type"))
        allow_messages = from_bool(obj.get("allow_messages"))
        premium = from_bool(obj.get("premium"))
        driver_license_types = from_list(DriverLicenseType.from_dict, obj.get("driver_license_types"))
        accept_incomplete_resumes = from_bool(obj.get("accept_incomplete_resumes"))
        working_days = from_list(BillingType.from_dict, obj.get("working_days"))
        working_time_intervals = from_list(BillingType.from_dict, obj.get("working_time_intervals"))
        working_time_modes = from_list(BillingType.from_dict, obj.get("working_time_modes"))
        accept_temporary = from_bool(obj.get("accept_temporary"))
        return Vacancy(id, description, branded_description, key_skills, schedule, accept_handicapped, accept_kids,
                       experience, address, alternate_url, apply_alternate_url, code, department, employment, salary,
                       archived, name, insider_interview, area, created_at, published_at, employer,
                       response_letter_required, type, has_test, response_url, test, specializations, contacts,
                       billing_type, allow_messages, premium, driver_license_types, accept_incomplete_resumes,
                       working_days, working_time_intervals, working_time_modes, accept_temporary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(str(self.id))
        result["description"] = from_str(self.description)
        result["branded_description"] = from_str(self.branded_description)
        result["key_skills"] = from_list(lambda x: to_class(KeySkill, x), self.key_skills)
        result["schedule"] = to_class(BillingType, self.schedule)
        result["accept_handicapped"] = from_bool(self.accept_handicapped)
        result["accept_kids"] = from_bool(self.accept_kids)
        result["experience"] = to_class(BillingType, self.experience)
        result["address"] = to_class(Address, self.address)
        result["alternate_url"] = from_str(self.alternate_url)
        result["apply_alternate_url"] = from_str(self.apply_alternate_url)
        result["code"] = from_str(self.code)
        result["department"] = to_class(BillingType, self.department)
        result["employment"] = to_class(BillingType, self.employment)
        result["salary"] = to_class(Salary, self.salary)
        result["archived"] = from_bool(self.archived)
        result["name"] = from_str(self.name)
        result["insider_interview"] = to_class(InsiderInterview, self.insider_interview)
        result["area"] = to_class(Area, self.area)
        result["created_at"] = from_str(self.created_at)
        result["published_at"] = from_str(self.published_at)
        result["employer"] = to_class(Employer, self.employer)
        result["response_letter_required"] = from_bool(self.response_letter_required)
        result["type"] = to_class(BillingType, self.type)
        result["has_test"] = from_bool(self.has_test)
        result["response_url"] = from_none(self.response_url)
        result["test"] = to_class(Test, self.test)
        result["specializations"] = from_list(lambda x: to_class(Specialization, x), self.specializations)
        result["contacts"] = to_class(Contacts, self.contacts)
        result["billing_type"] = to_class(BillingType, self.billing_type)
        result["allow_messages"] = from_bool(self.allow_messages)
        result["premium"] = from_bool(self.premium)
        result["driver_license_types"] = from_list(lambda x: to_class(DriverLicenseType, x), self.driver_license_types)
        result["accept_incomplete_resumes"] = from_bool(self.accept_incomplete_resumes)
        result["working_days"] = from_list(lambda x: to_class(BillingType, x), self.working_days)
        result["working_time_intervals"] = from_list(lambda x: to_class(BillingType, x), self.working_time_intervals)
        result["working_time_modes"] = from_list(lambda x: to_class(BillingType, x), self.working_time_modes)
        result["accept_temporary"] = from_bool(self.accept_temporary)
        return result


class VacancyList:
    items: List[Vacancy]
    found: int
    pages: int
    per_page: int
    page: int
    clusters: None
    arguments: None
    alternate_url: str

    def __init__(self, items: List[Any], found: int, pages: int, per_page: int, page: int, clusters: None,
                 arguments: None, alternate_url: str) -> None:
        self.items = items
        self.found = found
        self.pages = pages
        self.per_page = per_page
        self.page = page
        self.clusters = clusters
        self.arguments = arguments
        self.alternate_url = alternate_url

    @staticmethod
    def from_dict(obj: Any) -> 'VacancyList':
        assert isinstance(obj, dict)
        items = from_list(lambda x: x, obj.get("items"))
        found = from_int(obj.get("found"))
        pages = from_int(obj.get("pages"))
        per_page = from_int(obj.get("per_page"))
        page = from_int(obj.get("page"))
        clusters = from_none(obj.get("clusters"))
        arguments = from_none(obj.get("arguments"))
        alternate_url = from_str(obj.get("alternate_url"))
        return VacancyList(items, found, pages, per_page, page, clusters, arguments, alternate_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: x, self.items)
        result["found"] = from_int(self.found)
        result["pages"] = from_int(self.pages)
        result["per_page"] = from_int(self.per_page)
        result["page"] = from_int(self.page)
        result["clusters"] = from_none(self.clusters)
        result["arguments"] = from_none(self.arguments)
        result["alternate_url"] = from_str(self.alternate_url)
        return result
