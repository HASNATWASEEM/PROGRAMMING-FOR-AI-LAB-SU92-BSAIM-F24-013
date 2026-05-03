from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_texts = ["I love it", "Hate this movie", "Amazing experience"]
training_labels = ["positive", "negative", "positive"]

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_texts)

classifier = MultinomialNB()
classifier.fit(X_train, training_labels)

new_review = ["I hate it"]
X_new = vectorizer.transform(new_review)
predicted_sentiment = classifier.predict(X_new)

print(predicted_sentiment[0])