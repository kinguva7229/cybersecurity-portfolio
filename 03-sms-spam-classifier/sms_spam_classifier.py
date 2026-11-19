import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics, tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("SMSSpamCollection.csv", header=None, encoding="latin-1")

texts = data.iloc[:, 1]
labels = data.iloc[:, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.20, random_state=0
)

logReg = LogisticRegression()
logReg.fit(X_train, y_train)
y_predict = logReg.predict(X_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_predict)
print("Logistic Regression")
print(cnf_matrix)
print("Accuracy:", metrics.accuracy_score(y_test, y_predict))
print("Precision:", metrics.precision_score(y_test, y_predict, pos_label="spam"))
print("Recall:", metrics.recall_score(y_test, y_predict, pos_label="spam"))
print("F1-score", metrics.f1_score(y_test, y_predict, pos_label="spam"))
print(metrics.classification_report(y_test, y_predict))

dtree = tree.DecisionTreeClassifier(random_state=0)
dtree.fit(X_train, y_train)
y_predict_dt = dtree.predict(X_test)

cnf_matrix_dt = metrics.confusion_matrix(y_test, y_predict_dt)
print("Decision Tree")
print(cnf_matrix_dt)
print("Accuracy:", metrics.accuracy_score(y_test, y_predict_dt))
print("Precision:", metrics.precision_score(y_test, y_predict_dt, pos_label="spam"))
print("Recall:", metrics.recall_score(y_test, y_predict_dt, pos_label="spam"))
print("F1-score", metrics.f1_score(y_test, y_predict_dt, pos_label="spam"))
print(metrics.classification_report(y_test, y_predict_dt))

class_names = [0, 1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
sns.heatmap(pd.DataFrame(cnf_matrix_dt), annot=True, cmap="YlGnBu", fmt="g")
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title("Decision Tree Confusion matrix", y=1.1)
plt.ylabel("Actual label")
plt.xlabel("Predicted label")
plt.savefig("images/decision_tree_confusion_matrix.png", dpi=150, bbox_inches="tight")
plt.show()
