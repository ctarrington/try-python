import math
import random
import pandas as pd
import numpy as np

from extract_title import add_title


def fill_na_preserve_distribution(data, key):
    mu = data[key].mean()
    sigma = data[key].std()
    na_count = data[key].isnull().sum()
    replacements = np.random.normal(mu, sigma, na_count)

    filled_in = data[key].apply(
        lambda x: random.choice(replacements) if math.isnan(x) else x)
    data[key] = filled_in


def split_random_rows(data, ratio):
    indexes = np.random.rand(len(data)) < ratio

    first = data[indexes]
    second = data[~indexes]

    return first, second


def split_features_labels(data):
    data_x = data.drop(['Survived'], axis=1, inplace=False)
    data_y = data['Survived']

    return data_x, data_y


def calculate_youth(row):
    value = 0

    if (math.isnan(row.Age) and (row.IsMiss or row.IsMaster)):
        value = 1
    elif (not row.IsBaby and row.Age < 18 and row.Sex == 'female'):
        value = 1
    elif (not row.IsBaby and row.Age < 16 and row.Sex == 'male'):
        value = 1

    return value


def calculate_baby(row):
    value = 0

    if (row.Age <= 5 and row.Sex == 'female'):
        value = 1
    elif (row.Age <= 6 and row.Sex == 'male'):
        value = 1

    return value


def calculate_adult(row):
    value = 1

    if (row.IsBaby or row.IsYouth or row.IsOld):
        value = 0

    return value


def calculate_has_cabin(row):
    value = 1

    if (not isinstance(row.Cabin, str) and row.Pclass == 3):
        value = 0

    return value


def condition_data(data, max_age):

    data['FamilyCount'] = data['SibSp'] + data['Parch'] + 1
    data['SingleFamilySize'] = np.where(data['FamilyCount'] == 1, 1, 0)
    data['SmallFamilySize'] = np.where(
        (data['FamilyCount'] > 1) & (data['FamilyCount'] < 5), 1, 0)
    data['LargeFamilySize'] = np.where(
        data['FamilyCount'] >= 5, 1, 0)

    data['Gender'] = pd.factorize(data['Sex'])[0]

    data['FirstClass'] = np.where(data['Pclass'] == 1, 1, 0)
    data['SecondClass'] = np.where(data['Pclass'] == 2, 1, 0)
    data['ThirdClass'] = np.where(data['Pclass'] == 3, 1, 0)
    data['HasCabin'] = data.apply(calculate_has_cabin, axis=1)

    add_title(data)
    data['IsMiss'] = np.where(data['Title'] == 'Miss', 1, 0)
    data['IsMrs'] = np.where(data['Title'] == 'Mrs', 1, 0)
    data['IsMr'] = np.where(data['Title'] == 'Mr', 1, 0)
    data['IsMaster'] = np.where(data['Title'] == 'Master', 1, 0)
    data['IsAuthority'] = np.where(data['Title'] == 'Authority', 1, 0)
    data['IsRoyal'] = np.where(data['Title'] == 'Royal', 1, 0)

    data['IsOld'] = np.where(data['Age'] > 50, 1, 0)
    data['IsBaby'] = data.apply(calculate_baby, axis=1)
    data['IsYouth'] = data.apply(calculate_youth, axis=1)
    data['IsAdult'] = data.apply(calculate_adult, axis=1)

    fill_na_preserve_distribution(data, 'Age')
    data['Age'] = data['Age'] / max_age

    data.drop(['Sex', 'PassengerId', 'Ticket', 'Fare', 'Name', 'Embarked',
               'FamilyCount', 'Cabin', 'Pclass', 'SibSp', 'Parch', 'Title'],
              axis=1, inplace=True)
    return data
