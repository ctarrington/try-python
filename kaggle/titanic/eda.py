import re
import pandas as pd
import seaborn as sns

from prepare_normalize import condition_data


def extract_title(raw):
    match = re.search('(.*, )(.*?)\\.', raw)
    raw_title = match.group(2)
    return raw_title


BASE_PATH = '~/github/try-python/kaggle/titanic'

train = pd.read_csv(BASE_PATH + '/train.csv')
test = pd.read_csv(BASE_PATH + '/test.csv')
test['Survived'] = None

g = sns.heatmap(train[['Survived', 'Age']].corr(
), annot=True, fmt=".2f", cmap="coolwarm")

max_age = train['Age'].max()
conditioned = condition_data(train, max_age)

first_class = train[train['FirstClass'] == 1]
print('no cabin first class', first_class[first_class['HasCabin'] == 0])
