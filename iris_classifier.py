# Project 3 — Iris Species Classifier
# Loads the Iris dataset, trains a K-Nearest Neighbors classification model,
# evaluates its accuracy and visualizes the species distribution.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return iris, df


def train_and_evaluate(iris):
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy * 100:.1f}%")


def plot(iris):
    colors = ['red', 'green', 'blue']
    plt.figure(figsize=(8, 6))
    for i in range(3):
        mask = iris.target == i
        plt.scatter(iris.data[mask, 0], iris.data[mask, 2],
                    color=colors[i], label=iris.target_names[i])
    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Petal length (cm)")
    plt.title("Iris Species Classification")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    iris, df = load_data()
    print(df.head(10))
    print(f"\nDataset size: {len(df)} flowers")
    print(f"Species: {iris.target_names}")
    train_and_evaluate(iris)
    plot(iris)