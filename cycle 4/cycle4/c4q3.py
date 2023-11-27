from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn import metrics

print("Name:Anumol Thomas\nRoll No:22MCA011\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\n")
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
algorithms = {'GaussianNB': GaussianNB(), 'BernoulliNB': BernoulliNB(), 'MultinomialNB': MultinomialNB()}
for algo_name, algo in algorithms.items():
    algo.fit(X_train, y_train)
    y_pred = algo.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    mislabeled_count = (y_test != y_pred).sum()
    mismatched_labels = y_test[y_test != y_pred]
    print(f'\nResults for {algo_name}:')
    print(f'Accuracy: {accuracy}')
    print(f'Number of mislabeled classifications: {mislabeled_count}')
    print(f'Class labels of mismatching records: {mismatched_labels}')