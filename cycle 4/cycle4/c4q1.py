from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
print("Name:Anumol Thomas\nRoll No:22MCA011\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\n")
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)
accuracy_scores = []
k_values = [3, 5, 7]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)
    print(f"Accuracy for k={k}: {accuracy}")
best_accuracy = max(accuracy_scores)
best_k = k_values[accuracy_scores.index(best_accuracy)]
print(f"\nBest accuracy: {best_accuracy} with k={best_k}")