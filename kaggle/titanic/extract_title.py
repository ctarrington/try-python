import re


ROYAL_TITLES = ['Don', 'Dona', 'Lady', 'Sir', 'the Counteess', 'Jonkheer']


def extract_title(raw):
    match = re.search('(.*, )(.*?)\\.', raw)
    raw_title = match.group(2)

    value = 'Other'
    if raw_title in ['Miss', 'Miss', 'Mlle', 'Ms']:
        value = 'Miss'
    elif raw_title in ['Mrs', 'Mme']:
        value = 'Mrs'
    elif raw_title in ['Mr']:
        value = 'Mr'
    elif raw_title in ['Master']:
        value = 'Master'
    elif raw_title in ['Dr', 'Capt', 'Col', 'Rev']:
        value = 'Authority'
    elif raw_title in ROYAL_TITLES:
        value = 'Royal'

    return value


def add_title(data):
    titles = data['Name'].apply(extract_title)
    data['Title'] = titles
