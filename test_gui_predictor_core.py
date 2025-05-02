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
def testPredictionIsPositive():
  Ts = format.input(28,24.5,1,'male','no','northeast')
  result = model.predict(Ts)[0]
  assert result > 0, "Prediction shold be positive" 
def testPredictionType():
  Ts = format.input(50,30.5,0,'female','yes','northwest')
  result = model.predict(Ts)[0]
  assert isinstance(prediction, float), "prediction should be a float"
 def testCsvWriteAndRead():
   file_name = "test_preductions.csv"
   test_data = [30, "male", 22.0, 0, "no", "northwest", "3200.45"]
   with open(file_name, 'w', newline = '') as file:
     writer = csv.writer(file)
     writer.writerow(["Age", "BMI", "Children", "Sex", "Smoker", "Region", "Prediction Cost"])
     writer.writerow(test_data)
   with open(file_name,'r') as file:
     reader = csv.reader(file)
     lines = list(reader)
   assert lines[1][0] == "30"
   assert lines[1][6] == "3200.45"
   os.remove(file_name)
def testInputFormatColumn():
  Ts = format.input(33,29.4,2,'male','yes','southwest')
    expected_columns = [
      'age', 'bmi', 'children',
      'sex_male','smoker_yes',
      'region_northwest','region_southwest','region_southeast'
    ]
  assert list(Ts.columns) == expected_columns

