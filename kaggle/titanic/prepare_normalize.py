import pandas as pd
import numpy as np

from extract_title import add_title


def split_features_labels(data):
    data_x = data.drop(['Survived'], axis=1, inplace=False)
    data_y = data['Survived']

    return data_x, data_y


def condition_data(data, mean_age, max_age):
    data['Age'].fillna(mean_age, inplace=True)
    data['Age'] = data['Age'] / max_age
    data['FamilyCount'] = data['SibSp'] + data['Parch'] + 1
    data['SingleFamilySize'] = np.where(data['FamilyCount'] == 1, 1, 0)
    data['SmallFamilySize'] = np.where(
        (data['FamilyCount'] > 1) & (data['FamilyCount'] < 5), 1, 0)
    data['Gender'] = pd.factorize(data['Sex'])[0]
    data['FirstClass'] = np.where(data['Pclass'] == 1, 1, 0)
    data['SecondClass'] = np.where(data['Pclass'] == 2, 1, 0)
    data['ThirdClass'] = np.where(data['Pclass'] == 3, 1, 0)

    add_title(data)
    data['IsMiss'] = np.where(data['Title'] == 'Miss', 1, 0)
    data['IsMrs'] = np.where(data['Title'] == 'Mrs', 1, 0)
    data['IsMr'] = np.where(data['Title'] == 'Mr', 1, 0)
    data['IsMaster'] = np.where(data['Title'] == 'Master', 1, 0)
    data['IsAuthority'] = np.where(data['Title'] == 'Authority', 1, 0)

    data.drop(['Sex', 'PassengerId', 'Ticket', 'Fare', 'Name', 'Embarked',
               'FamilyCount', 'Cabin', 'Pclass', 'SibSp', 'Parch',
               'Title'],
              axis=1, inplace=True)
    return data
