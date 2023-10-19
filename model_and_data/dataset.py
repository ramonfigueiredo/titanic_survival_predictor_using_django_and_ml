import numpy as np
import pandas as pd


def read_dataset():
    # Read dataset CSV file
    dataset = pd.read_csv('train.csv', encoding='latin-1')

    # Apply lower case in all the dataset columns text
    dataset = dataset.rename(columns=lambda x: x.strip().lower())

    # Print dataset head (first lines)
    print(dataset.head())

    # Move the 'Survived' column to the last column
    # Remove the columns: 'PassengerId', 'Name', 'Ticket', and 'Cabin'
    dataset = dataset[['pclass', 'sex', 'age', 'sibsp',
                       'parch', 'fare', 'embarked', 'survived']]

    # Convert the text 'male' to 0 and 'female' to 1
    dataset['sex'] = dataset['sex'].map({'male': 0, 'female': 1})

    # Convert all the lines in the column 'Age' to numeric values
    # Replace the blank = nan values (not a number) to the mean value in all lines in the column 'Age'
    dataset['age'] = pd.to_numeric(dataset['age'], errors='coerce')
    dataset['age'] = dataset['age'].fillna(np.mean(dataset['age']))

    # Encoding the column 'Embarked' (C, Q or S) values to numbers
    # Embarked is port of embarkation and it is a categorical feature which has 3 unique values (C, Q or S):
    # C = Cherbourg
    # Q = Queenstown
    # S = Southampton
    embarked_dummies = pd.get_dummies(dataset['embarked'])
    dataset = pd.concat([dataset, embarked_dummies], axis=1)

    # Drop embarked column
    dataset = dataset.drop(['embarked'], axis=1)

    return dataset
