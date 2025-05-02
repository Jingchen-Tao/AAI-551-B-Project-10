# Author: Jingchen Tao, Olin Dsouza, Smit Minekumar Desai
# Date: 2025/5/02

#File description:
#This is a Python script for training a prediction model for health insurance costs. It reads data containing age, gender,
# BMI, smoking, region, and other information from insurance.csv files, preprocesses the data
# (such as monothermal coding of categorical variables such as gender and region), constructs features and labels, and trains them with a linear regression model.
# After the training is complete, the script outputs the performance evaluation metrics of the model (including the R² score and mean square error)
# and saves the model as a insurance_model.pkl file for API program calling.






#improvement:This improvement adds model evaluation metrics (R² and Mean Square Error (MSE) to the model training script,
# so that the model performance is no longer in the training and use stage, but has basic explanatory and credibility verification.
# At the same time, the categorical variables in the original data are numerized through One-Hot encoding,
# which effectively avoids the trap of dummy variables and enhances the expressive ability of the model. Finally,
# the model is persisted and saved using joblib,which is convenient for GUI modules to be called directly,
# which improves the modularity and reusability of the project.




# Import necessary libraries
import pandas as pd                                      # For data manipulation
from sklearn.model_selection import train_test_split     # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression        # Linear regression model
from sklearn.metrics import r2_score, mean_squared_error # For evaluating model performance
import joblib                                            # For saving the trained model

# -------------------------------
# Step 1: Load and preprocess data
# -------------------------------

# Load the health insurance dataset from CSV file
df = pd.read_csv("insurance.csv")

# Convert categorical variables (sex, smoker, region) into dummy/indicator variables using one-hot encoding
# drop_first=True removes the first category to avoid multicollinearity (dummy variable trap)
df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

# Separate input features (X) and the target variable (y)
X = df.drop("charges", axis=1)   # Features: all columns except 'charges'
y = df["charges"]                # Target: insurance charges

# -------------------------------
# Step 2: Split the dataset
# -------------------------------

# Split data into training and testing sets (80% train, 20% test)
# random_state ensures reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Step 3: Train the model
# -------------------------------

# Initialize and train a linear regression model using the training data
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Step 4: Evaluate the model
# -------------------------------

# Predict the charges on the test set
y_pred = model.predict(X_test)

# Evaluate performance using R² score and Mean Squared Error (MSE)
r2 = r2_score(y_test, y_pred)                     # R²: how well the model explains variance (1.0 = perfect)
mse = mean_squared_error(y_test, y_pred)          # MSE: average squared prediction error

# Print evaluation results
print(f"Model Evaluation:")
print(f"  R² Score: {r2:.4f}")                    # Display R² score with 4 decimal precision
print(f"  Mean Squared Error: {mse:.2f}")         # Display MSE with 2 decimal precision

# -------------------------------
# Step 5: Save the trained model
# -------------------------------

# Save the trained model to a file for future use
joblib.dump(model, "insurance_model.pkl")
print("Model has been trained and saved as insurance_model.pkl")
