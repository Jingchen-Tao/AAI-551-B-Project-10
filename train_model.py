# 作者(author): 陶景晨 (Jingchen Tao)
# CWID: 20030105
#2025/4/05
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv("insurance.csv")


df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)


X = df.drop("charges", axis=1)
y = df["charges"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


joblib.dump(model, "insurance_model.pkl")
print("模型已训练并保存为 insurance_model.pkl")
