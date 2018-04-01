import pandas as pd

from sklearn import svm

from prepare_normalize import condition_data, split_features_labels

BASE_PATH = '~/github/try-python/kaggle/titanic'

all_train = pd.read_csv(BASE_PATH + '/train.csv')
all_train = condition_data(all_train)

print('tuned, trained on ALL')
tuned_clf = svm.SVC(C=9.1e5, gamma=1e-3)
all_train_x, all_train_y = split_features_labels(all_train)
tuned_clf.fit(all_train_x, all_train_y)

print('create predictions')
test = pd.read_csv(BASE_PATH + '/test.csv')
conditioned = condition_data(test.copy())
test['Survived'] = tuned_clf.predict(conditioned)

print('write predictions')
test.drop(['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket',
           'Fare', 'Cabin', 'Embarked'], axis=1, inplace=True)
test.to_csv(BASE_PATH + '/predictions.csv', index=False)
print('done')
