# Diabetes Management Suite

## Overview
Welcome to the Diabetes Management Suite, a comprehensive toolkit for diabetes prediction and data analysis. This suite consists of two main components: a Jupyter Notebook for in-depth analysis and visualization of diabetes data, and a "Diabetes Prediction App" built with Django.

### About the Dataset
- **Source:** National Institute of Diabetes and Digestive and Kidney Diseases
- **Patients:** Female individuals, at least 21 years old, of Pima Indian heritage
- **Features:** The dataset includes several features such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age, and Outcome.

#### Columns in the Dataset:
- **Pregnancies:** Number of times pregnant
- **Glucose:** Plasma glucose concentration
- **BloodPressure:** Diastolic blood pressure
- **SkinThickness:** Triceps skin fold thickness
- **Insulin:** 2-Hour serum insulin
- **BMI:** Body Mass Index
- **DiabetesPedigreeFunction:** A function determining likelihood of diabetes based on family history
- **Age:** Age of the patient
- **Outcome:** Indicates whether the patient has diabetes (1) or not (0)

## Projects

### 1. Diabetes Data Analysis and Visualization (Jupyter Notebook)
A detailed Jupyter Notebook offering a comprehensive analysis of the diabetes dataset, including data preprocessing, visualization, and predictive model evaluation.

#### Notebook Contents:
- **Data Cleaning and Preprocessing:** Essential steps to prepare the data for analysis.
- **Exploratory Data Analysis:** In-depth analysis with visualizations to understand data patterns and relationships.
- **Logistic Regression Model:** Training the model and assessing its accuracy.

#### Technologies Used:
- Jupyter Notebook
- Python
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Missingno

### 2. Diabetes Prediction App (Django Web Application)
A Django-based web application that predicts the likelihood of diabetes using a logistic regression model. This app allows users to input their health metrics and receive real-time predictions.

#### App Features:
- **Interactive Form:** Users can enter their medical data such as blood pressure, glucose levels, etc.
- **Real-time Prediction Output:** Instant results showing the likelihood of diabetes.
- **Logistic Regression Model:** Utilizes the Pima Indian Diabetes Database for predictions.

#### Technologies Used:
- Django
- Python
- HTML/CSS
- Machine Learning Library: Scikit-Learn

## Getting Started
To use this suite, clone the repository to your local machine. Ensure you have Python installed, along with the necessary libraries mentioned under each project.
