import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

df =pd.read_csv('collegePlace.csv',index_col = False )
df =df.iloc[:, [3, 4, 7]]
import matplotlib.pyplot as plt
plt.scatter(df['Internships'], df['CGPA'], c=df['PlacedOrNot'])
plt.xlabel('Internships')
plt.ylabel('CGPA')
plt.title('Internships vs CGPA (Colored by Placement)')
plt.show()

X= df.iloc[:,0:2]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
X_train= sc.fit_transform(X_train)

X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
lr =LogisticRegression()
lr.fit(X_train, y_train)

y_pred =lr.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, y_train.values, clf=lr, legend=2)

import pickle

pickle.dump(lr,open('model2005.pkl','wb'))

# Ensure "models" folder exists
os.makedirs("models", exist_ok=True)

# Save model
model_path = os.path.join("models", "model2005.pkl")
joblib.dump(model, model_path)

print(f"✅ Model saved at {model_path}")
