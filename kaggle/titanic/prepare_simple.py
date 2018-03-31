import pandas as pd
from extract_title import add_title


def split_features_labels(data):
    data_x = data.drop(['Survived'], axis=1, inplace=False)
    data_y = data['Survived']

    return data_x, data_y


def condition_data(data, mean_age):
    data['Age'].fillna(mean_age, inplace=True)
    data['FamilyCount'] = data['SibSp'] + data['Parch'] + 1
    data['Gender'] = pd.factorize(data['Sex'])[0]
    data['PassengerClass'] = pd.factorize(data['Pclass'])[0]

    add_title(data)
    data['TitleCategory'] = pd.factorize(data['Title'])[0]

    data.drop(['Sex', 'PassengerId', 'Ticket', 'Fare', 'Name', 'Embarked',
               'Cabin', 'FamilyCount', 'Pclass', 'SibSp', 'Parch', 'Title'],
              axis=1, inplace=True)
    return data
