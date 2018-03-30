import pandas as pd
import numpy as np

from sklearn import svm
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import classification_report

from prepare import condition_data, split_features_labels

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
train, validation = split_random_rows(all_train, 0.7)

train_x, train_y = split_features_labels(all_train)
validation_x, validation_y = split_features_labels(validation)

c_ints = [9.07e5, 9.08e5, 9.09e5, 9.1e5, 9.11e5]

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-2, 1e-3],
                     'C': c_ints, 'degree': [2]}]

scores = ['precision', 'recall']

kfolds = StratifiedKFold(n_splits=5, shuffle=True)

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=kfolds,
                       n_jobs=-1, scoring='%s_macro' % score)
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
