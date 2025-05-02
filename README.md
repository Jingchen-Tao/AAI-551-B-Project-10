# Health Insurance Cost Predictor

**Author**: Jingchen Tao, Olin Dsouza, Smit Minekumar Desai  
**Date**: 2025/05/02

---

## 📌 Project Overview

This project consists of a **graphical interface application** and a **model training script** developed in Python to predict **health insurance costs** based on user-provided personal information such as age, BMI, smoking status, etc.

The app is designed for **user-friendliness**, **modularity**, and **data transparency**, and includes advanced features like **real-time predictions**, **PDF export**, **theme switching**, and **graphical visualizations**.

---

## 🎯 Features

### ✅ GUI Application (`gui_predictor.py`)

- Built with **Tkinter** and **TTK widgets** for modern styling
- Soft yellow themed background with optional **Dark Mode toggle**
- Input fields:
  - Age
  - BMI
  - Number of Children
  - Sex (male/female)
  - Smoker (yes/no)
  - Region (northeast/northwest/southeast/southwest)
- **Buttons and Functions**:
  - 🧠 **Predict**: Predict insurance cost using the trained regression model
  - 📋 **Clear**: Reset all input fields
  - ❌ **Exit**: Close the app
  - 📂 **Open CSV**: Open the prediction history file
  - 🕒 **Last Prediction**: Show the most recent prediction in a popup
  - 📊 **Show Chart**: Visualize prediction history using Matplotlib
  - 🧾 **Save as PDF**: Export the last prediction to a neatly formatted PDF file
  - 🌙 **Toggle Theme**: Switch between Light and Dark modes for improved user experience
- **CSV logging**: All predictions are saved to `user_predictions.csv`
- **Logo support** (`logo.png`) for custom branding

---

### ✅ Model Training Script (`train_model.py` or similar)

- Reads and processes data from `insurance.csv`
- Handles:
  - One-hot encoding of categorical variables (sex, smoker, region)
  - Splits into features and target labels (`charges`)
- Trains a **Linear Regression model**
- Outputs:
  - **R² Score**
  - **Mean Squared Error (MSE)**
- Saves the trained model as `insurance_model.pkl` using `joblib`
- Designed for reuse in GUI-based prediction apps

---

## 💾 Files in the Project

| Filename              | Description                                           |
|-----------------------|-------------------------------------------------------|
| `gui_predictor.py`    | Main GUI application for predictions                  |
| `train_model.py`      | Model training script using Linear Regression         |
| `insurance.csv`       | Dataset used for training                             |
| `insurance_model.pkl` | Saved model file used by GUI                          |
| `user_predictions.csv`| Auto-generated CSV logging user predictions           |
| `logo.png`            | (Optional) Image displayed in the GUI header          |
| `README.md`           | This file                                             |
| `requirements.txt`    | List of Python dependencies (optional but recommended)|

---

## 🖼️ Sample Output (PDF)

After making a prediction, users can click **“Save as PDF”** and generate a file containing:

- Age, BMI, Sex
- Smoker status, Region
- Predicted Insurance Cost
- Exported as a neat, readable PDF

---

## 🌓 Light & Dark Theme

You can switch between a light yellow theme and a dark background using the **"Toggle Theme"** button in the GUI.  
This improves accessibility and user comfort, especially in low-light environments.

---

## 🛠️ Dependencies

Make sure to install the following libraries:

```bash
pip install pandas matplotlib joblib reportlab scikit-learn
