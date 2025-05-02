import pytest
import pandas as pd
import joblib
import os
import csv

model = joblib.load("insurance_model.pk1")

def creatInput(age, bmi, children, sex, smoker, region):
  (
  "age": [age],
  "bmi" : [bmi],
  "children" : [children],
  "sex" : [1 if sex == 'male' else 0],
  "smoker" : [1 if smoker == 'yes' else 0],
  "region_northwest" : [1 if region == 'northwest' else 0],
  "region_southwest" : [1 if region == 'southwest' else 0],
  "region_southeast" : [1 if region == 'southeast' else 0],
  ) return pd.DataFrame
