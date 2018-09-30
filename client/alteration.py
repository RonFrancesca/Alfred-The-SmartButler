import re


def detectYears(input):
    YEAR_REGEX = re.compile(r'(\b)(\d\d)([1-9]\d)(\b)')
    return YEAR_REGEX.sub('\g<1>\g<2> \g<3>\g<4>', input)


def clean(input):
    return detectYears(input)
