import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score

df = pd.read_csv("IMDB Dataset.csv", sep=',')
stopset = set(stopwords.words('english'))
vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents=ascii, stop_words=stopset)

y = df.sentiment
X=vectorizer.fit_transform(df.review)

X_train, X_test, y_train,y_test = train_test_split(X,y)
clf = naive_bayes.MultinomialNB()
clf.fit(X_train,y_train)

pos = 0
neg = 0
no_of_rev = 0

f = open('reviews.txt', 'r')
f1 = f.readlines()
for x in f1:
    no_of_rev = no_of_rev + 1
    array = np.array([x])
    vector = vectorizer.transform(array)
    if clf.predict(vector) == 'positive':
        pos = pos + 1
    else:
        neg = neg + 1

print(str(pos * 100 / no_of_rev) + "%")
print(str(neg * 100 / no_of_rev) + "%")