import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

base_path = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(base_path + '/train.csv')

max_age = all_train['Age'].max()
mean_age = all_train['Age'].mean()

def condition_data(td):
    td['Age'].fillna(mean_age, inplace = True)
    td['Age'] /= max_age 

    td['FamilyCount'] = td['SibSp'] + td['Parch'] + 1
    td['SingleFamilySize'] = np.where(td['FamilyCount'] == 1, 1, 0)
    td['SmallFamilySize'] = np.where((td['FamilyCount'] > 1) & (td['FamilyCount'] < 5), 1, 0)
    td['Gender'] = pd.factorize(td['Sex'])[0]
    td['FirstClass'] = np.where(td['Pclass'] == 1, 1, 0)
    td['SecondClass'] = np.where(td['Pclass'] == 2, 1, 0)
    td['ThirdClass'] = np.where(td['Pclass'] == 3, 1, 0)

    td.drop(['Sex', 'PassengerId', 'Ticket', 'Fare', 'Name', 'Embarked', 'FamilyCount', 'Cabin', 'Pclass', 'SibSp', 'Parch'], axis=1,inplace=True)
    return td
    
all_train = condition_data(all_train)
indexes = np.random.rand(len(all_train)) < 0.8

train = all_train[indexes]
validation = all_train[~indexes]

train_x = all_train.drop(['Survived'], axis=1, inplace=False)
train_y = all_train['Survived']

validation_x = validation.drop(['Survived'], axis=1, inplace=False)
validation_y = validation['Survived']

gnb = GaussianNB()
model = gnb.fit(train_x, train_y)

predicted_y = gnb.predict(validation_x)

print(accuracy_score(validation_y, predicted_y))

validation['Prediction'] = predicted_y

# print(validation)