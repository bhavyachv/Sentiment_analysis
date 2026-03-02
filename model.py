import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib 

# Load Data
df=pd.read_csv('reviews.csv')

#Convert Text to Numbers (Vectorization)
vectorizer=CountVectorizer(stop_words='english')
X=vectorizer.fit_transform(df['Review'])
y = df['Sentiment']

#train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model=MultinomialNB()
model.fit(X_train,y_train)

joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Model trained and saved!")