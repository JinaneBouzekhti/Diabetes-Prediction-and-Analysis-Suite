from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Your views and other code follow here

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def Predict(request):
    return render(request, 'Predict.html')

def result(request):
    data = pd.read_csv("C:/Users/hp/Desktop/Intership/2nd_Project/Diabetes Prediction/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    
    pared = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if pared == [1]:
        result1 = "This person is diabetic"
    elif pared == [0]:
        result1 = 'This person is not diabetic'

    return render(request,"Predict.html", {"result2": result1})
