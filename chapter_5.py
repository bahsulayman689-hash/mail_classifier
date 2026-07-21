import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import re
import warnings as wr
wr.filterwarnings("ignore")

def absolute_tokenizer(text):
    return re.findall(r'\w+|[\W\s]', text)

raw_mail_data = pd.read_csv("mail_data.csv")
print(raw_mail_data.head())
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')
print(mail_data.head())
print(mail_data.shape)
#TODO:label encoder of the categorical columns
#o--> spam
#1--> ham
mail_data["Category"] = mail_data['Category'].map({"spam":0, "ham": 1})
print(mail_data.head())

#seperating the text and label

X = mail_data["Message"]

Y = mail_data["Category"]

print(X)

print(Y)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.2,
                                                    random_state=3)
print(X.shape)
print(X_train.shape)
print(X_test.shape)
#Convert the numerical value for the computer to understand concept
#feature extraction



feature_extraction = TfidfVectorizer(min_df=1, 
                                     stop_words=None,
                                     lowercase=False,
                                     
                                     ngram_range=(1, 2),
                                     token_pattern=None,
                                     tokenizer=absolute_tokenizer)

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

#convert the y_train and y_Test

y_train = y_train.astype('int')
y_test = y_test.astype('int')

print(X_train_features)

model = LogisticRegression(random_state=42,
                           class_weight='balanced',
                           C=0.5,
                           max_iter=1000)

model.fit(X_train_features, y_train)

y_pred = model.predict(X_train_features)
accuracy_of_training = accuracy_score(y_train, y_pred)
print(f"the accuracy of the model is {accuracy_of_training}")
print(f"the confusion_metrix of the model train {confusion_matrix(y_train, y_pred)}")
y_pred_test = model.predict(X_test_features)
accuracy_of_test = accuracy_score(y_test, y_pred_test)
print(f"the accuracy of the model is {accuracy_of_test}")
print(f"the confusion metrix of the testing {confusion_matrix(y_test, y_pred_test)} ")

cm = confusion_matrix(y_test, y_pred_test)
plt.figure(figsize=(9, 4))
sns.heatmap(
    cm,
    fmt='d',
    annot=True,
    cbar=False,
    cmap='Set1',
    xticklabels=["Spam", "Ham"],
    yticklabels=["Spam", "ham"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Spam Detection Confusion Matrix")
plt.show()

cm = confusion_matrix(y_train, y_pred)
plt.figure(figsize=(9, 4))
sns.heatmap(
    cm,
    fmt='d',
    annot=True,
    cbar=False,
    cmap='Set2',
    xticklabels=["spam", "ham"],
    yticklabels=["spam", "ham"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Spam Detection Confusion Matrix")
plt.show()

input_mail = ("WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.")

input_mail_features = feature_extraction.transform([input_mail])


if input_mail_features.nnz == 0:
    print("🚨 Security Warning: This text contains zero words recognized by the model vocabulary!")

else: 
    prediction = model.predict(input_mail_features)
    print(prediction)
    if (prediction[0] == 1):
    
        print("✅ the message you recieve is ham mail")
    else:
        print("🚨the mesaage you recieve is spam mail")

joblib.dump(model, "Mail_test.pkl")
joblib.dump(feature_extraction, "feature_test.pkl")

model = joblib.load("Mail_test.pkl")
feature_extraction = joblib.load("feature_test.pkl")