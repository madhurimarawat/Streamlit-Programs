# Regression is used to find real values
# It gives a general formula for the dataset
# In this we calculate how much the difference in between the predicted value and the actual value for the whole dataset
# Difference between actual value and predicted value is called cost function
# Error is calculated for entire dataset using this cost function

# Importing Libraries

# Importing Numpy
import numpy as np
# To read CSV file
import pandas as pd
# For importing algorithm
from sklearn.linear_model import LinearRegression
# For splitting between training and testing
from sklearn.model_selection import train_test_split
# Importing accuracy score and mean_squared_error
from sklearn.metrics import mean_squared_error, accuracy_score,mean_absolute_error
# For plotting
import matplotlib.pyplot as plt
# Importing streamlit for deployment
import streamlit as st

st.title("Salary Prediction Using Linear Regression")

# Implementing Simple Linear Regression for salary dataset
# This dataset contains the years of experience and Salary of employees
# First column dosen't have any significance in data (Only used for Index)
# We can remove that
# To remove that we have two options

# Method 1-By giving usecols arguments and only using required columns
data=pd.read_csv("Salary_dataset.csv",usecols=['YearsExperience','Salary'])
print(data)

# Method 2-By using the index_col and setting it to 0 so that it doesn't take index
data=pd.read_csv("Salary_dataset.csv",index_col=0)
print(data)

# Preprocessing
# Splitting between Input and Output
X,Y=data['YearsExperience'].to_numpy().reshape(-1,1),data['Salary'].to_numpy().reshape(-1,1)
print("Input is:\n",X)
print("\nOutput is:\n",Y)
print("Shape of Input data is:",X,"Shape of Output data is:",Y)

# Splitting into training and testing data
# we can do this directly as dataset is small instead of using train test split
x_train=X[:-5]
x_test=X[-5:]
y_train=Y[:-5]
y_test=Y[-5:]
print("Training data is:\n",x_train)
print("\nTesting data is:\n",y_train)
print("Shape of Training data is:",x_train.shape,"Shape of Testing data is:",y_train.shape)

# Choosing algorithm
reg=LinearRegression()
# Training data
reg.fit(x_train,y_train)

# Evaluating model
print("Training Accuracy score is:",reg.score(x_train,y_train)*100)
# Checking predicted values
predict=reg.predict(x_test)
print("Predicted values are:\n")
print(predict)
# Checking predicted value for given value
print("Predicted value for 1.5 is:\n",reg.predict([[1.5]]))

# print(accuracy_score(predict,y_test))-Doesn't work as accuracy score doesn't take array

# Checking for Error
print("Mean Squared error is:",mean_squared_error(y_test,predict))
print("Mean Absolute error is:",mean_absolute_error(y_test,predict))

# Plotting
# We can see the points are much away from the line
# Cost function is very high
# This is why absolute and mean squared error is so high
# This plot will be in the main page
st.subheader("This is the Final Plot for this Linear Regression Algorithm")
fig=plt.figure()
plt.scatter(x_test,y_test,color="blue")
plt.plot(x_test,predict,color="red")
plt.title("Regression Plot of Years of Experience VS Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend(['Actual Values','Best Line or General formula'])
st.pyplot(fig)

# Sidebar is used so that it displays this in left side 
exp = st.sidebar.text_input("Enter Experience")
 
# Display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.sidebar.button('Submit')):

    result=reg.predict([[int(exp)]])
    # Rounding off Output to 3 decimal values using the numpy round function (Since this is a numpy array we cannot use round function for integers)
    output = np.round(result[0],3)

    st.sidebar.success("Employee Salary Should be $ {}".format(float(output)))