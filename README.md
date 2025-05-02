# Author: Jingchen Tao, Olin Dsouza , Smit Minekumar Desai
# Date: 2025/5/2

#File description:
#This is a graphical interface program built on Tkinter, users can enter personal information (such as age, BMI, number of children,
# gender, whether they smoke, location) in the interface, click the "Predict" button, the program will call the pre-trained model to make a cost prediction,
# and display the results in a pop-up window. At the same time, all forecast records are automatically saved to a CSV file.
# The interface also provides functions such as clearing inputs, exiting programs, opening history, viewing the latest forecast results,
# and displaying historical cost forecast changes in charts and graphs, improving user interactivity and data visualization experience.

#improvement:The original interface had simple predictions,
# but now the version not only beautifies the interface (with TTK controls and a soft yellow background),
# but also adds useful features such as clearing inputs, exiting with one click,
# opening history files, displaying the results of the most recent predictions,and more.
# In addition, the program has added a new visualization function for historical forecast data (plotting using matplotlib),
# which further improves the user experience and presentation.
# All predictions are automatically written to a CSV file and negative values are automatically avoided,
# making the system more robust and useful.

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
