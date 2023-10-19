import time

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from dataset import read_dataset


def run_cross_validation(classifier, X_train, y_train, n_folds=5):
    print()
    print('*' * 100)
    print('{}-Fold Cross Validation'.format(n_folds))
    print('*' * 100)

    accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=n_folds)
    print("Accuracy in each of the {} folds:".format(n_folds))
    for acc in accuracies:
        print('\t', round(acc * 100, 2), end=' ')

    print("\n\nAverage accuracy after {}-Fold Cross Validation: {}%".format(n_folds, round(accuracies.mean() * 100, 2)))

    print("\nAverage standard deviation after {}-Fold Cross Validation: {}%".format(n_folds, round(accuracies.std() * 100, 2)))

    print('*' * 100)


def print_metrics(y_test, y_pred):
    print()
    print('*' * 100)
    print('Confusion Matrix Metrics')
    print('*' * 100)

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix\n", cm)

    # Calculating metrics using the confusion matrix
    TP = cm[0][0]
    FN = cm[0][1]
    TN = cm[1][0]
    FP = cm[1][1]

    print()

    print("True Positive (TP):", TP)
    print("False Negative (FN):", FN)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)

    print()

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    print("Accuracy = (TP + TN) / (TP + TN + FP + FN): %.2f %%" % (accuracy * 100))
    recall = TP / (TP + FN)
    print("Recall = TP / (TP + FN): %.2f %%" % (recall * 100))
    precision = TP / (TP + FP)
    print("Precision = TP / (TP + FP): %.2f %%" % (precision * 100))
    Fmeasure = (2 * recall * precision) / (recall + precision)
    print("Fmeasure = (2 * recall * precision) / (recall + precision): %.2f %%" % (Fmeasure * 100))

    print('*' * 100)


if __name__ == '__main__':
    start_time = time.time()

    # Read dataset
    dataset = read_dataset()

    # Split dataset in 'training' set (X) and 'test' set (y)
    X = dataset.drop(['survived'], axis=1)
    y = dataset['survived']

    # Normalize data in value from 0 to 1
    sc = MinMaxScaler(feature_range=(0, 1))
    X = sc.fit_transform(X)

    # RandomForestClassifier
    classifier = LogisticRegression(C=1, n_jobs=-1)

    # Train the model
    start_training = time.time()
    classifier.fit(X, y)
    print('The training took {:.2f} seconds'.format(time.time() - start_training))

    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Print classification report
    print('*' * 100)
    print("Classification report")
    print('*' * 100)
    print(classification_report(y_test, y_pred, target_names=['Jobs will succeed', 'Jobs will fail']))

    # Print metrics
    print_metrics(y_test, y_pred)

    # Applying k-Fold Cross Validation
    run_cross_validation(classifier, X_train, y_train)

    print('Done! It took {:.2f} seconds'.format(time.time() - start_time))
