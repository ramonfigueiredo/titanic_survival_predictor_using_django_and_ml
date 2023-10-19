import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

from dataset import read_dataset

if __name__ == '__main__':
    # Read dataset
    dataset = read_dataset()

    # Split dataset in 'training' set (X) and 'test' set (y)
    X = dataset.drop(['survived'], axis=1)
    y = dataset['survived']

    # Normalize data in value from 0 to 1
    sc = MinMaxScaler(feature_range=(0, 1))
    X_scaled = sc.fit_transform(X)

    # Logistic Regression (aka logit, MaxEnt) classifier.
    classifier = LogisticRegression(C=1, n_jobs=-1)

    # Train the LogisticRegression model
    classifier.fit(X_scaled, y)

    # Export the LogisticRegression model
    pickle.dump(classifier, open("../titanic/ml_model.sav", "wb"))

    # Export the MinMaxScaler
    pickle.dump(sc, open("../titanic/scaler.sav", "wb"))
