import pandas as pd

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, \
    GradientBoostingClassifier, BaggingClassifier
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

predictions = pd.read_csv(BASE_PATH + '/test.csv')
predictions.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
                  'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)

svc_scenario = {'name': 'svc',
                'default_model': svm.SVC(),
                'tuned_parameters': [{'kernel': ['rbf'],
                                      'gamma': [1e-2, 1e-3, 1e-4, 1e-5],
                                      'C': [8e4, 9e4, 1e5, 2e5, 3e5],
                                      'degree': [2]}]}

forest_scenario = {'name': 'forest',
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
                   ]}

ada_scenario = {'name': 'ada-boost',
                'default_model': AdaBoostClassifier(),
                'tuned_parameters': [
                    {'n_estimators': [50, 75, 100, 125, 150],
                     'learning_rate': [0.05, 0.1, 0.25, 0.5, 1]}
                ]}

gradient_scenario = {'name': 'gradient-boost',
                     'default_model': GradientBoostingClassifier(),
                     'tuned_parameters': [
                         {'n_estimators': [50, 75, 100, 125, 150],
                          'learning_rate': [0.05, 0.1, 0.25, 0.5, 1],
                          'max_depth': [2, 3, 4, 5]}
                     ]}

bagging_scenario = {'name': 'bagging',
                    'default_model': BaggingClassifier(),
                    'tuned_parameters': [
                        {'n_estimators': [50, 75, 100, 125, 150],
                         'oob_score': [True, False]}
                    ]}

scenarios = [
    svc_scenario,
    # forest_scenario,
    # ada_scenario,
    # gradient_scenario,
    # bagging_scenario
]

scenario_counter = 0
for scenario in scenarios:
    name = scenario['name'] + str(scenario_counter)
    scenario_counter += 1

    print('starting grid', name)

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
    predictions[name] = test_predicted
    test.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
               'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)
    test.to_csv(BASE_PATH + '/predictions-' +
                name + '-grid.csv', index=False)
    print('done', name)
    print()


def tally_votes(row):
    average = sum(row) / len(row)
    if (average > 0 and average < 1):
        print('mismatched row', row)

    return 1 if average > 0.5 else 0


print('tallying votes')
without_passenger_id = predictions.drop(['PassengerId'], axis=1, inplace=False)
without_passenger_id['Survived'] = without_passenger_id.apply(
    tally_votes, axis=1)
print(without_passenger_id)
predictions['Survived'] = without_passenger_id['Survived']
predictions = predictions[['PassengerId', 'Survived']]
predictions.to_csv(BASE_PATH + '/predictions-votes.csv', index=False)
print('done tallying votes')
