#(author):Jenchen Tao CWID: 20030105
#(author):Olin Dsouza :20033076
#(author):Smit Desai :20035929
#2025/4/10
#The program is a health insurance cost predictor where users can enter personal information
# and the program predicts insurance costs based on a trained linear regression model.
#The information entered includes: age, BMI, number of children, gender, smoking status, and region.
# The prediction results will be displayed on the interface and saved to a CSV file.

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import csv


model = joblib.load("insurance_model.pkl")


def predict():
    try:
        age = int(entry_age.get())
        bmi = float(entry_bmi.get())
        children = int(entry_children.get())
        sex = var_sex.get()
        smoker = var_smoker.get()
        region = var_region.get()


        input_dict = {
            'age': [age],
            'bmi': [bmi],
            'children': [children],
            'sex_male': [1 if sex == 'male' else 0],
            'smoker_yes': [1 if smoker == 'yes' else 0],
            'region_northwest': [1 if region == 'northwest' else 0],
            'region_southeast': [1 if region == 'southeast' else 0],
            'region_southwest': [1 if region == 'southwest' else 0],
        }
        input_df = pd.DataFrame(input_dict)

        prediction = model.predict(input_df)[0]
        messagebox.showinfo("预测结果(Predict the outcome)", f"预测保险费用为(Forecast the cost of insurance)：${prediction:.2f}")

        with open("user_predictions.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([age, sex, bmi, children, smoker, region, prediction])

    except Exception as e:
        messagebox.showerror("错误(False)", f"输入错误(False Input)：{e}")


root = tk.Tk()
root.title("健康保险费用预测器(Health Insurance Cost Predictor)")

tk.Label(root, text="年龄（age）").grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

tk.Label(root, text="BMI").grid(row=1, column=0)
entry_bmi = tk.Entry(root)
entry_bmi.grid(row=1, column=1)

tk.Label(root, text="子女数量（numbers of children）").grid(row=2, column=0)
entry_children = tk.Entry(root)
entry_children.grid(row=2, column=1)

tk.Label(root, text="性别（sex）").grid(row=3, column=0)
var_sex = tk.StringVar(value="male")
tk.OptionMenu(root, var_sex, "male", "female").grid(row=3, column=1)

tk.Label(root, text="是否吸烟（smoke）").grid(row=4, column=0)
var_smoker = tk.StringVar(value="no")
tk.OptionMenu(root, var_smoker, "yes", "no").grid(row=4, column=1)

tk.Label(root, text="地区（region）").grid(row=5, column=0)
var_region = tk.StringVar(value="northeast")
tk.OptionMenu(root, var_region, "northeast", "northwest", "southeast", "southwest").grid(row=5, column=1)

tk.Button(root, text="预测（predict）", command=predict).grid(row=6, columnspan=2, pady=10)

root.mainloop()

