# 
# Patrick Smurla
# Indpendent Research
# This is a program that will test a dataset to see how accurate it is in detecting phising
# or scams from emails.
#

#Importing needed resources
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

#Main function
def init():
    #Read the CSV file
    data = pd.read_csv('svmtext.csv', header = 0, engine = 'python')
    print("Reading the dataset...")

    #Data preprocessing
    X = data.drop('Class', axis = 1)
    y = data['Class']

    #Split data into Test and Train
    print("Dividing the dataset into testing and training sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

    #Training the model
    print("Training started...")
    svclassifier = SVC(kernel = 'linear')
    svclassifier.fit(X_train, y_train)
    print("Training Completed.")

    #Predictions
    y_pred = svclassifier.predict(X_test)
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

#Calling the main function
init()
