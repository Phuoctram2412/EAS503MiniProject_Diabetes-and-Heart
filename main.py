import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the csv file 
df_diabetes = pd.read_csv('diabetes_dataset.csv')


## Pre-processing data
# check to see if there is missing value in the diabetes dataset
df_diabetes.isna().sum() # return 0 hence the dataset has no missing value

# we want to test to see if blood pressure is different whether the patients have diabetes or not by create 2 dataset below where 1 is patients with diabetes and 0 is patients without diabetes
without_diabetes = df_diabetes[df_diabetes['Outcome'] == 0]
with_diabetes = df_diabetes[df_diabetes['Outcome'] == 1]



## Diabetes vs Family History Bar Graph
family_hist = with_diabetes['FamilyHistory'].value_counts() # Return 2885 for 1 indicated a 'Yes' and 397 for 0 indicated a 'No'
# Plotting the bar graph
plt.figure(figsize=(8, 6))
family_hist.plot(kind='bar', color=['skyblue', 'lightcoral'])

# Adding labels and title
plt.title('Diabetes vs Family History', fontsize=16)
plt.xlabel('Family History', fontsize=16)
plt.ylabel('Diabetes', fontsize=16)
plt.xticks([0, 1], ['Family History with Diabetes', 'Family History with no Diabetes'], rotation=0)

# Display the plot
plt.show()



## Glucose levels vs HbA1c
# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Patients without diabetes
ax1.scatter(without_diabetes['Glucose'], without_diabetes['HbA1c'])
ax1.set_xlabel('Glucose Levels', fontsize=16)
ax1.set_ylabel('HbA1c', fontsize=16)
ax1.set_title('Glucose vs HbA1c for patients without diabetes', fontsize=16)
z1 = np.polyfit(without_diabetes['Glucose'], without_diabetes['HbA1c'], 1)
p1 = np.poly1d(z1)
ax1.plot(without_diabetes['Glucose'], p1(without_diabetes['Glucose']), "r--")

# Patients with diabetes
ax2.scatter(with_diabetes['Glucose'], with_diabetes['HbA1c'])
ax2.set_xlabel('Glucose Levels', fontsize=16)
ax2.set_ylabel('HbA1c', fontsize=16)
ax2.set_title('Glucose vs HbA1c for patients with diabetes', fontsize=16)
z2 = np.polyfit(with_diabetes['Glucose'], with_diabetes['HbA1c'], 1)
p2 = np.poly1d(z2)
ax2.plot(with_diabetes['Glucose'], p2(with_diabetes['Glucose']), "r--")

# Display the plots
plt.tight_layout()
plt.show()





### Glucose levels vs HDL/LDL
# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Patients without diabetes
ax1.scatter(with_diabetes['Glucose'], with_diabetes['LDL'])
ax1.set_xlabel('Glucose Levels', fontsize=16)
ax1.set_ylabel('LDL', fontsize=16)
ax1.set_title('Glucose vs LDL for patients with diabetes', fontsize=16)
z1 = np.polyfit(with_diabetes['Glucose'], with_diabetes['LDL'], 1)
p1 = np.poly1d(z1)
ax1.plot(with_diabetes['Glucose'], p1(with_diabetes['Glucose']), "r--")

# Patients with diabetes
ax2.scatter(with_diabetes['Glucose'], with_diabetes['HDL'])
ax2.set_xlabel('Glucose Levels', fontsize=16)
ax2.set_ylabel('HDL', fontsize=16)
ax2.set_title('Glucose vs HDL for patients with diabetes', fontsize=16)
z2 = np.polyfit(with_diabetes['Glucose'], with_diabetes['HDL'], 1)
p2 = np.poly1d(z2)
ax2.plot(with_diabetes['Glucose'], p2(with_diabetes['Glucose']), "r--")

# Display the plots
plt.tight_layout()
plt.show()




### Glucose levels vs Blood Pressure
# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Patients without diabetes
ax1.scatter(without_diabetes['Glucose'], without_diabetes['BloodPressure'])
ax1.set_xlabel('Glucose Levels', fontsize=16)
ax1.set_ylabel('Blood Pressure', fontsize=16)
ax1.set_title('Glucose vs Blood Pressure for patients without diabetes', fontsize=16)
z1 = np.polyfit(without_diabetes['Glucose'], without_diabetes['BloodPressure'], 1)
p1 = np.poly1d(z1)
ax1.plot(without_diabetes['Glucose'], p1(without_diabetes['Glucose']), "r--")

# Patients with diabetes
ax2.scatter(with_diabetes['Glucose'], with_diabetes['BloodPressure'])
ax2.set_xlabel('Glucose Levels', fontsize=16)
ax2.set_ylabel('Blood Pressure', fontsize=16)
ax2.set_title('Glucose vs Blood Pressure for patients with diabetes', fontsize=16)
z2 = np.polyfit(with_diabetes['Glucose'], with_diabetes['BloodPressure'], 1)
p2 = np.poly1d(z2)
ax2.plot(with_diabetes['Glucose'], p2(with_diabetes['Glucose']), "r--")

# Display the plots
plt.tight_layout()
plt.show()






### Glucose levels vs BMI levels
# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# Patients without diabetes
ax1.scatter(without_diabetes['Glucose'], without_diabetes['BMI'])
ax1.set_xlabel('Glucose Levels', fontsize=16)
ax1.set_ylabel('BMI', fontsize=16)
ax1.set_title('Glucose vs BMI for patients without diabetes', fontsize=16)
z1 = np.polyfit(without_diabetes['Glucose'], without_diabetes['BMI'], 1)
p1 = np.poly1d(z1)
ax1.plot(without_diabetes['Glucose'], p1(without_diabetes['Glucose']), "r--")

# Patients with diabetes
ax2.scatter(with_diabetes['Glucose'], with_diabetes['BMI'])
ax2.set_xlabel('Glucose Levels', fontsize=16)
ax2.set_ylabel('BMI', fontsize=16)
ax2.set_title('Glucose vs BMI for patients with diabetes', fontsize=16)
z2 = np.polyfit(with_diabetes['Glucose'], with_diabetes['BMI'], 1)
p2 = np.poly1d(z2)
ax2.plot(with_diabetes['Glucose'], p2(with_diabetes['Glucose']), "r--")

# Display the plots
plt.tight_layout()
plt.show()
