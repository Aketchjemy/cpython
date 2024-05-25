import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

texts = ["I love this movie", "This movie is great", "I dislike this movie", "I hate this movie"]
var = "I enjoy this movie", "This movie is fun", "This movie is boring","I detest this movie"
labels = [1, 1, 0, 0]  # 1 for positive sentiment, 0 for negative sentiment

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train_vec, y_train)

# Train SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_vec, y_train)

# Train Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vec, y_train)

# Predict using each classifier
knn_pred = knn_classifier.predict(X_test_vec)
svm_pred = svm_classifier.predict(X_test_vec)
nb_pred = nb_classifier.predict(X_test_vec)

# Evaluate performance
print("K-Nearest Neighbors Classifier:")
print("Accuracy:", accuracy_score(y_test, knn_pred))
print("Classification Report:")
print(classification_report(y_test, knn_pred))

print("\nSupport Vector Machine Classifier:")
print("Accuracy:", accuracy_score(y_test, svm_pred))
print("Classification Report:")
print(classification_report(y_test, svm_pred))

print("\nNaive Bayes Classifier:")
print("Accuracy:", accuracy_score(y_test, nb_pred))
print("Classification Report:")
print(classification_report(y_test, nb_pred))



    
