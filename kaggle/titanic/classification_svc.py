import pandas as pd
import numpy as np

from sklearn import svm
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import classification_report

from prepare_normalize import condition_data, split_features_labels

BASE_PATH = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(BASE_PATH + '/train.csv')

max_age = all_train['Age'].max()
mean_age = all_train['Age'].mean()


def split_random_rows(data, ratio):
    indexes = np.random.rand(len(data)) < ratio

    first = data[indexes]
    second = data[~indexes]

    return first, second


all_train = condition_data(all_train, mean_age, max_age)
train, validation = split_random_rows(all_train, 0.8)

train_x, train_y = split_features_labels(all_train)
validation_x, validation_y = split_features_labels(validation)

c_ints = [9.04e5, 9.05e5, 9.06e5, 9.07e5, 9.08e5]

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-5],
                     'C': c_ints, 'degree': [2]}]

kfolds = StratifiedKFold(n_splits=5, shuffle=True)

print('starting grid')

clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=kfolds,
                   n_jobs=-1, scoring='accuracy')
clf.fit(train_x, train_y)

print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print(clf.best_score_)
print()

print('trained via k-folds against hold out')
predicted_y = clf.predict(validation_x)
print(classification_report(validation_y, predicted_y))


print('default, trained on whole and run against hold out')
default_clf = svm.SVC()
default_clf.fit(train_x, train_y)
print(classification_report(validation_y, default_clf.predict(validation_x)))

print('tuned, trained on whole and run against hold out')
tuned_clf = svm.SVC(C=9.1e5, gamma=1e-3)
tuned_clf.fit(train_x, train_y)
print(classification_report(validation_y, tuned_clf.predict(validation_x)))

print('write predictions')
test = pd.read_csv(BASE_PATH + '/test.csv')
test_conditioned = condition_data(test.copy(), mean_age, max_age)

test_predicted = clf.predict(test_conditioned)
test['Survived'] = test_predicted
test.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
           'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)
test.to_csv(BASE_PATH + '/predictions.csv', index=False)
print('done')
