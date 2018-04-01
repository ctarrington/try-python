import pandas as pd

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import classification_report

from prepare_normalize import condition_data, split_features_labels, \
    split_random_rows

BASE_PATH = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(BASE_PATH + '/train.csv')

max_age = all_train['Age'].max()
mean_age = all_train['Age'].mean()

all_train = condition_data(all_train, max_age)
train, validation = split_random_rows(all_train, 0.9)

train_x, train_y = split_features_labels(all_train)
validation_x, validation_y = split_features_labels(validation)

kfolds = StratifiedKFold(n_splits=5, shuffle=True)

scenarios = [
    {'name': 'svc',
     'default_model': svm.SVC(),
     'tuned_parameters': [{'kernel': ['rbf'],
                           'gamma': [1e-2, 1e-3, 1e-4, 1e-5],
                           'C': [8e4, 9e4, 1e5, 2e5, 3e5],
                           'degree': [2]}]},
    {'name': 'forest',
     'default_model': RandomForestClassifier(),
     'tuned_parameters': [
         {'n_estimators': [150, 200, 250, 300, 350],
          'min_samples_split': [3, 4, 5],
          'bootstrap': [True],
          'oob_score': [True]},

         {'n_estimators': [40, 60, 80, 100],
          'min_samples_split': [3, 4],
          'bootstrap': [True, False],
          'oob_score': [False]}
     ]
     }
]

for scenario in scenarios:
    print('starting grid', scenario['name'])

    clf = GridSearchCV(scenario['default_model'],
                       scenario['tuned_parameters'],
                       cv=kfolds,
                       n_jobs=-1,
                       scoring='accuracy')
    clf.fit(train_x, train_y)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print(clf.best_score_)
    print()

    print('trained via grid, against hold out')
    print(classification_report(validation_y, clf.predict(validation_x)))

    print('write predictions')
    test = pd.read_csv(BASE_PATH + '/test.csv')
    test_conditioned = condition_data(test.copy(), max_age)
    test_predicted = clf.predict(test_conditioned)
    test['Survived'] = test_predicted
    test.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
               'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)
    test.to_csv(BASE_PATH + '/predictions-' +
                scenario['name'] + '-grid.csv', index=False)
    print('done', scenario['name'])
    print()
