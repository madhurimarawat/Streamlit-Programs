# Naive-Bayes Classifier-Supervised Learning Algorithm
# Mainly used for text classification
# Based on Bayes Theorem
# Seeing Accuracy of model for various datasets

# Importing Numpy
import numpy as np
# To read csv file
import pandas as pd
# For splitting between training and testing
from sklearn.model_selection import train_test_split
# Importing Algorithm
from sklearn.naive_bayes import GaussianNB
# For checking/Evaluating accuracy of model and printing the confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix
# For Plotting
import matplotlib.pyplot as plt
# Importing streamlit for deployment
import streamlit as st

st.title("Diabetes Detection Using Naive Bayes Classifier Algorithm")

# Data Gathering
# Glucose and blood pressure as input and diabetes as output
# Model will predict if person is diabetic or not

data=pd.read_csv("Naive-Bayes-Classification-Data.csv")
print("Data is:\n",data)
print("Information about Dataframe is:\n",data.info)

# Data Preprocessing is not required as data is already cleaned
# Splitting between Input(X) and Output(Y)
X,Y=data.drop("diabetes",axis=1),data['diabetes']
print("Input is:\n",X,"\n","Output is:\n",Y)
# Splitting data into training and testing
x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size=0.8)
print("Shape of x_train(training data) for dataset is:",x_train.shape,"Shape of y_train(testing data) for dataset is:",y_train.shape)

# Choosing algorithm
nb=GaussianNB()
# Training the model
nb.fit(x_train,y_train)

# Evaluating/Testing the model
print("Training Accuracy is:",nb.score(x_train,y_train)*100)
predicted_data=nb.predict(x_test)
print("Predicted Data is:\n",predicted_data)
print("Testing Accuracy is:",accuracy_score(y_test,predicted_data)*100)
# Printing Confusion Matrix
print("Confusion Matrix is:\n",confusion_matrix(y_test,predicted_data))

st.write(f'Classifier : Naive Bayes Classifier')
st.write(f'Shape of Dataset is:  {data.shape}')
st.write('Number of classes: ', len(np.unique(Y)))
st.write("Accuracy :  ",accuracy_score(y_test,predicted_data)*100)


# Define a mapping for colors based on labels (1 for diabetic, 0 for not diabetic)
color_map = {1: 'red', 0: 'blue'}

# Create a list of colors corresponding to each data point
colors = [color_map[label] for label in Y]

# Because this dataset has a lot of overlapping points
# Add a small amount of jitter to the data points
jittered_glucose = X["glucose"] + np.random.normal(0, 0.5, len(X))
jittered_bloodpressure = X["bloodpressure"] + np.random.normal(0, 0.5, len(X))

# Increase point size to make them more visible
point_size = 20  # Adjust the size as needed

# Create the scatter plot
st.subheader("This is the Final Plot for this Dataset")
fig = plt.figure()
scatter = plt.scatter(jittered_glucose, jittered_bloodpressure, c=colors, alpha=0.8, s=point_size)
plt.xlabel("Glucose")
plt.ylabel("Blood Pressure")

# Create a legend with labels "Diabetic" and "Not Diabetic"
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=("Diabetic" if label == 1 else "Not Diabetic")) for label, color in color_map.items()]
plt.legend(handles=handles, title='Diabetic')

plt.title("Graph showing whether a patient is diabetic or not")
st.pyplot(fig)

# Sidebar is used so that it displays this in left side 
glu = st.sidebar.text_input("Enter Glucose")
bp = st.sidebar.text_input("Enter Blood Pressure")
# Display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.sidebar.button('Submit')):

    output=nb.predict([[int(glu),int(bp)]])

    # Since Output values will be 0 for not diabetic and 1 for diabetic we have to print according to that
    if output==0:
        st.sidebar.success('Diabetes Prediction is: Not Diabetic')
    else:
        st.sidebar.error('Diabetes Prediction is: Diabetic')
