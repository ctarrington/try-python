import re


def extract_title(raw):
    match = re.search('(.*, )(.*)\\.', raw)
    raw_title = match.group(2)
    if raw_title in ['Miss', 'Miss', 'Mlle', 'Ms']:
        return 'Miss'
    if raw_title in ['Mrs', 'Mme']:
        return 'Mrs'
    if raw_title in ['Mr']:
        return 'Mr'
    if raw_title in ['Master']:
        return 'Master'
    if raw_title in ['Dr', 'Captain', 'Col', 'Rev']:
        return 'Authority'

    return 'Other'


def add_title(data):
    titles = data['Name'].apply(extract_title)
    data['Title'] = titles
