import pandas as pd
import numpy as np

from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

base_path = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(base_path + '/train.csv')

max_age = all_train['Age'].max()
mean_age = all_train['Age'].mean()

def split_random_rows(td, ratio):
    indexes = np.random.rand(len(td)) < 0.8

    first = td[indexes]
    second = td[~indexes]

    return first, second


def split_features_labels(td):
    td_x = td.drop(['Survived'], axis=1, inplace=False)
    td_y = td['Survived']

    return td_x, td_y


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
train, validation = split_random_rows(all_train, 0.8)

train_x, train_y = split_features_labels(all_train)
validation_x, validation_y = split_features_labels(validation)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-3, 1e-4, 1e-5],
                     'C': [1e5, 1e6, 1e7]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=3, n_jobs=-1, scoring='%s_macro' % score)
    clf.fit(train_x, train_y)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print(clf.best_score_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
                % (mean, std * 2, params))
    print()         



    predicted_y = clf.predict(validation_x)
    print(classification_report(validation_y, predicted_y))



print('default, trained on whole train against hold out')
default_clf = svm.SVC()
default_clf.fit(train_x, train_y)
print(classification_report(validation_y, default_clf.predict(validation_x)))

print('tuned, trained on whole train against hold out')
tuned_clf = svm.SVC(C=1000000, gamma=0.001)
tuned_clf.fit(train_x, train_y)
print(classification_report(validation_y, tuned_clf.predict(validation_x)))