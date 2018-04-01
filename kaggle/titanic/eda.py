import re
import pandas as pd

from prepare_normalize import condition_data


def extract_title(raw):
    match = re.search('(.*, )(.*?)\\.', raw)
    raw_title = match.group(2)
    return raw_title


BASE_PATH = '~/github/try-python/kaggle/titanic'

train = pd.read_csv(BASE_PATH + '/train.csv')
test = pd.read_csv(BASE_PATH + '/test.csv')
test['Survived'] = None

all_data = train.append(test)
titles = all_data['Name'].apply(extract_title)
print(pd.unique(titles))
print(extract_title('Rothschild, Mrs. Martin (Elizabeth L. Barrett)'))


third_class = all_data['Pclass'] == 3
has_cabin = all_data['Cabin'].notnull()

third_with_cabin = all_data[third_class & has_cabin]
print(third_with_cabin)

age_max = all_data['Age'].max()
age_avg = all_data['Age'].mean()
age_std = all_data['Age'].std()
print('age: ', age_avg, age_std)
print('na count', all_data['Age'].isnull().sum())

condition_data(all_data, age_max)
age_avg = all_data['Age'].mean()
age_std = all_data['Age'].std()
print('age: ', age_avg, age_std)
print('na count', all_data['Age'].isnull().sum())

print(all_data)
