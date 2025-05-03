# Health Insurance Cost Predictor

## Project Description

This project implements a desktop-based health insurance cost prediction tool using a machine learning model trained on demographic and lifestyle data. The model estimates insurance charges based on user-provided inputs such as age, body mass index (BMI), smoking status, and region. A graphical user interface (GUI) is provided for user interaction, and results can be saved, visualized, and exported.

## Components

1. **`train_model.py`**
   This script reads the dataset (`insurance.csv`), performs data preprocessing using one-hot encoding on categorical variables (`sex`, `smoker`, `region`), and trains a linear regression model to predict insurance charges. The trained model is saved as `insurance_model.pkl`.

2. **`gui_predictor.py`**
   This script defines the main application GUI using Tkinter. It loads the trained model, collects user input, performs prediction, displays the result, and saves prediction data to a CSV file. Additional features include:

   * Input reset and application exit buttons
   * View and open previous predictions
   * Visualize prediction history using `matplotlib`
   * Export the most recent prediction as a PDF
   * Light/dark theme toggle
   * Optional logo support

3. **`test_gui_predictor_core.py`**
   This script includes unit tests that verify the following aspects:

   * Model prediction returns positive float values
   * Input formatting matches the model's expected schema
   * CSV write/read operations function correctly

4. **`insurance.csv`**
   The dataset used for model training. It includes information on age, sex, BMI, number of children, smoking status, region, and insurance charges.

5. **`user_predictions.csv`**
   A generated file that stores all user inputs and corresponding predicted insurance costs for future reference and visualization.

6. **`logo.png`**
   An optional image file used as a visual identifier at the top of the GUI window.

## Model Information

* Model Type: Linear Regression
* Evaluation Metrics:

  * R² Score (coefficient of determination)
  * Mean Squared Error (MSE)
* Encoding: One-hot encoding for categorical variables with `drop_first=True`

## Usage Instructions

1. Run `train_model.py` to generate the trained model file (`insurance_model.pkl`).
2. Run `gui_predictor.py` to launch the graphical interface.
3. Enter the requested inputs and click **Predict** to view and save results.
4. Use the additional GUI buttons to:

   * Clear inputs
   * Open past results
   * View most recent prediction
   * Visualize prediction history
   * Export to PDF
   * Switch theme

## Dependencies

* Python 3.7+
* Required packages:

  * `pandas`
  * `scikit-learn`
  * `joblib`
  * `matplotlib`
  * `tkinter` (standard library)
  * `Pillow`
  * `reportlab`
  * `pytest` (for testing)

Install dependencies via pip:

```
pip install pandas scikit-learn joblib matplotlib Pillow reportlab pytest
```

## Acknowledgements

This project was developed by Jingchen Tao, Olin Dsouza, and Smit Minekumar Desai as part of coursework in CS 442/561.
