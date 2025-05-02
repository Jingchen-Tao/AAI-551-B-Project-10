# Author: Jingchen Tao, Olin Dsouza , Smit Minekumar Desai
# Date: 2025/5/2

# Description:
# A GUI to predict health insurance cost using a trained ML model, with CSV logging,
# visual history, and enhanced styling including logo banner.

import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import joblib
import csv
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageTk  # ← For logo image support

# Load the pre-trained model
try:
    model = joblib.load("insurance_model.pkl")
except FileNotFoundError:
    messagebox.showerror("Model Error", "Trained model file not found. Please train the model first.")
    exit()

# Create header if needed
def write_csv_header_if_needed():
    if not os.path.exists("user_predictions.csv"):
        with open("user_predictions.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Age", "Sex", "BMI", "Children", "Smoker", "Region", "Predicted Cost"])

# Prediction logic
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
        raw_prediction = model.predict(input_df)[0]
        prediction = abs(raw_prediction)

        messagebox.showinfo("Prediction Result", f"Predicted Insurance Cost: ${prediction:.2f}")

        write_csv_header_if_needed()
        with open("user_predictions.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([age, sex, bmi, children, smoker, region, f"{prediction:.2f}"])

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Clear input fields
def clear_inputs():
    entry_age.delete(0, tk.END)
    entry_bmi.delete(0, tk.END)
    entry_children.delete(0, tk.END)
    var_sex.set("male")
    var_smoker.set("no")
    var_region.set("northeast")

# Exit the GUI
def exit_app():
    root.destroy()

# Open CSV file
def open_csv():
    if os.path.exists("user_predictions.csv"):
        os.startfile("user_predictions.csv")
    else:
        messagebox.showwarning("File Not Found", "No prediction file found yet.")

# Show last prediction
def show_recent_prediction():
    try:
        df = pd.read_csv("user_predictions.csv")
        last_row = df.iloc[-1]
        result = (f"Last Prediction:\nAge: {last_row['Age']}, Sex: {last_row['Sex']}, "
                  f"BMI: {last_row['BMI']}, Children: {last_row['Children']},\n"
                  f"Smoker: {last_row['Smoker']}, Region: {last_row['Region']}, "
                  f"Cost: ${last_row['Predicted Cost']}")
        messagebox.showinfo("Latest Prediction", result)
    except Exception:
        messagebox.showinfo("No Data", "No prediction data available.")

# Show cost chart
def show_chart():
    try:
        df = pd.read_csv("user_predictions.csv")
        plt.figure(figsize=(8, 4))
        plt.plot(df["Predicted Cost"], marker='o', linestyle='-')
        plt.title("Prediction History")
        plt.xlabel("Prediction #")
        plt.ylabel("Insurance Cost ($)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception:
        messagebox.showinfo("No Data", "No prediction data to plot.")

# GUI layout and widgets
def create_gui():
    global root
    root = tk.Tk()
    root.title("Health Insurance Cost Predictor")
    root.configure(bg="#fffacd")
    root.geometry("420x500")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TLabel", font=("Segoe UI", 10), background="#fffacd")
    style.configure("TButton", font=("Segoe UI", 10, "bold"))
    style.configure("TCombobox", font=("Segoe UI", 10))

    # ==== Add Logo at Top ====
    try:
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((200, 60))
        logo = ImageTk.PhotoImage(logo_image)
        logo_label = ttk.Label(root, image=logo)
        logo_label.image = logo  # Keep a reference
        logo_label.grid(row=0, column=0, columnspan=2, pady=10)
    except:
        pass  # No logo found, skip

    # ==== Inputs ====
    ttk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global entry_age
    entry_age = ttk.Entry(root)
    entry_age.grid(row=1, column=1, padx=10)

    ttk.Label(root, text="BMI:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    global entry_bmi
    entry_bmi = ttk.Entry(root)
    entry_bmi.grid(row=2, column=1, padx=10)

    ttk.Label(root, text="Number of Children:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    global entry_children
    entry_children = ttk.Entry(root)
    entry_children.grid(row=3, column=1, padx=10)

    ttk.Label(root, text="Sex:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    global var_sex
    var_sex = tk.StringVar(value="male")
    ttk.Combobox(root, textvariable=var_sex, values=["male", "female"], state="readonly").grid(row=4, column=1, padx=10)

    ttk.Label(root, text="Smoker:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    global var_smoker
    var_smoker = tk.StringVar(value="no")
    ttk.Combobox(root, textvariable=var_smoker, values=["yes", "no"], state="readonly").grid(row=5, column=1, padx=10)

    ttk.Label(root, text="Region:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    global var_region
    var_region = tk.StringVar(value="northeast")
    ttk.Combobox(root, textvariable=var_region, values=["northeast", "northwest", "southeast", "southwest"], state="readonly").grid(row=6, column=1, padx=10)

    # ==== Buttons ====
    ttk.Button(root, text="Predict", command=predict).grid(row=7, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="Clear", command=clear_inputs).grid(row=8, column=0, pady=5)
    ttk.Button(root, text="Exit", command=exit_app).grid(row=8, column=1, pady=5)
    ttk.Button(root, text="Open CSV", command=open_csv).grid(row=9, column=0, pady=5)
    ttk.Button(root, text="Last Prediction", command=show_recent_prediction).grid(row=9, column=1, pady=5)
    ttk.Button(root, text="Show Chart", command=show_chart).grid(row=10, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


  

