# Health Insurance Cost Predictor

**Author**: Jingchen Tao, Olin Dsouza, Smit Minekumar Desai  
**Date**: 2025/05/02

---

## 📌 Project Overview

This project consists of a **graphical interface application** and a **model training script** developed in Python to predict **health insurance costs** based on user-provided personal information such as age, BMI, smoking status, etc.

The app is designed for **user-friendliness**, **modularity**, and **data transparency**, and includes advanced features like **real-time predictions**, **PDF export**, and **graphical visualizations**.

---

## 🎯 Features

### ✅ GUI Application (`gui_predictor.py`)

- Built with **Tkinter** and **TTK widgets** for modern styling
- Soft yellow themed background and professional layout
- Input fields:
  - Age
  - BMI
  - Number of Children
  - Sex (male/female)
  - Smoker (yes/no)
  - Region (northeast/northwest/southeast/southwest)
- Predict button to calculate insurance cost using a **trained regression model**
- **Popup output** with predicted result
- **CSV logging**: Automatically stores all prediction records in `user_predictions.csv`
- **"Last Prediction"** shows the latest predicted data from CSV
- **"Show Chart"** visualizes historical prediction trends with Matplotlib
- **"Save as PDF"** feature to export the most recent prediction with a user-chosen filename
- **"Open CSV"** to launch the full prediction history file
- **"Clear"** and **"Exit"** controls
- **Logo support** (`logo.png`) for branded appearance

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

| Filename | Description |
|----------|-------------|
| `gui_predictor.py` | Main GUI application for predictions |
| `train_model.py` | Model training script using Linear Regression |
| `insurance.csv` | Dataset used for training |
| `insurance_model.pkl` | Saved model file used by GUI |
| `user_predictions.csv` | Auto-generated CSV logging user predictions |
| `logo.png` | (Optional) Image displayed in the GUI header |
| `requirements.txt` | List of dependencies (if created manually) |

---

## 🖼️ Sample Output (PDF)

After making a prediction, users can click **“Save as PDF”** and generate a file containing:

- Age, BMI, Sex
- Smoker status, Region
- Predicted Insurance Cost
- Exported as a neat, readable PDF

---

## 🛠️ Dependencies

Make sure to install the following libraries:

```bash
pip install pandas matplotlib joblib reportlab scikit-learn


