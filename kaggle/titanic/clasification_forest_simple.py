import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from prepare_simple import condition_data, split_features_labels

BASE_PATH = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(BASE_PATH + '/train.csv')

max_age = all_train['Age'].max()
mean_age = all_train['Age'].mean()


def split_random_rows(data, ratio):
    indexes = np.random.rand(len(data)) < ratio

    first = data[indexes]
    second = data[~indexes]

    return first, second


all_train = condition_data(all_train, mean_age)
train, validation = split_random_rows(all_train, 0.90)

train_x, train_y = split_features_labels(all_train)
validation_x, validation_y = split_features_labels(validation)

clf = RandomForestClassifier(n_estimators=100, oob_score=True)
clf.fit(train_x, train_y)
print('Out-of-bag score estimate: ', clf.oob_score_)

print('trained via k-folds against hold out')
print(classification_report(validation_y, clf.predict(validation_x)))

print('trained via k-folds against whole train')
print(classification_report(train_y, clf.predict(train_x)))


print('write predictions')
test = pd.read_csv(BASE_PATH + '/test.csv')
test_conditioned = condition_data(test.copy(), mean_age)

test_predicted = clf.predict(test_conditioned)
test['Survived'] = test_predicted
test.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
           'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)
test.to_csv(BASE_PATH + '/predictions.csv', index=False)
print('done')
