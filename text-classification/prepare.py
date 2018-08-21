import json

import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

from sklearn.preprocessing import LabelEncoder


def _convert_row_to_text(row, key):
    text = " ".join(row[key])
    return text


def _convert_column_to_text(data, key):
    data[key] = data.apply(_convert_row_to_text, axis=1, key=key)


def read_and_normalize(file):
    with open(file) as raw_file:
        raw_json = json.load(raw_file)
        normalized = json_normalize(raw_json)
        return normalized


def prepare(vectorizer, labeled_data, unlabeled_data, text_key, label_key):
    _convert_column_to_text(labeled_data, text_key)
    _convert_column_to_text(unlabeled_data, text_key)

    labeled_occurances = vectorizer.fit_transform(labeled_data[text_key])
    unlabeled_occurances = vectorizer.transform(unlabeled_data[text_key])

    encoder = LabelEncoder()
    labels = encoder.fit_transform(labeled_data[label_key])

    return labeled_occurances, unlabeled_occurances, labels, encoder

