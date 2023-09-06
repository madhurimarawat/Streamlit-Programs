# In this program we will apply various ML algorithms to the built in datasets in scikit-learn

# Importing required Libraries
# Importing Numpy
import numpy as np
# To read csv file
import pandas as pd
# Importing datasets from sklearn
from sklearn import datasets
# For splitting between training and testing
from sklearn.model_selection import train_test_split
# Importing Algorithm for Simple Vector Machine
from sklearn.svm import SVC
# Importing Knn algorithm
from sklearn.neighbors import KNeighborsClassifier
# Importing  Decision Tree algorithm
from sklearn.tree import DecisionTreeClassifier
# Importing Random Forest Classifer
from sklearn.ensemble import RandomForestClassifier
# Importing Naive Bayes algorithm
from sklearn.naive_bayes import GaussianNB
# Importing Linear and Logistic Regression
from sklearn.linear_model import LinearRegression,LogisticRegression
# Importing accuracy score and mean_squared_error
from sklearn.metrics import mean_squared_error, accuracy_score,mean_absolute_error
# Importing PCA for dimension reduction
from sklearn.decomposition import PCA
# For Plotting
import matplotlib.pyplot as plt
import seaborn as sns
# For model deployment
import streamlit as st

# Giving Title
st.title("ML Algorithms on Inbuilt Datasets")

# Now we are making a select box for dataset
data_name=st.sidebar.selectbox("Select Dataset",
                  ("Iris","Breast Cancer","Wine","Diabetes","Digits"))

# The Next is selecting algorithm
# We will display this in the sidebar
algorithm=st.sidebar.selectbox("Select Supervised Learning Algorithm",
                     ("KNN","SVM","Decision Tree","Naive Bayes","Random Forest","Linear Regression","Logistic Regression"))

# Now we need to load the builtin dataset
# This is done using the load_dataset_name function
def load_dataset(Data):

    # Using Switch case by match in python
    match Data:
        case "Iris":
            return datasets.load_iris()
        case "Wine":
            return datasets.load_wine()
        case "Breast Cancer":
            return datasets.load_breast_cancer()
        case "Diabetes":
            return datasets.load_diabetes()
        case default:
            return datasets.load_digits()

# Now we need to call function to load the dataset
data=load_dataset(data_name)

# Now after this we need to split between input and output
# We use data.data as we need to copy data to X which is Input
X = data.data
# Since this is built in dataset we can directly load output or target class by using data.target function
Y = data.target

# Adding Parameters so that we can select from various parameters
def add_parameter(algorithm):

    # Declaring a dictionary for storing parameters
    params = dict()

    # Deciding parameters based on algorithm
    match algorithm:

        # Adding paramters for SVM
        case 'SVM':

             # Adding regularization parameter from range 0.01 to 10.0
             c_regular = st.sidebar.slider('C (Regularization)', 0.01, 10.0)
             # Kernel is the arguments in the ML model
             # Polynomial ,Linear, Sigmoid and Radial Basis Function are types of kernals which we can add
             kernel_custom = st.sidebar.selectbox('Kernel', ('linear', 'poly ', 'rbf', 'sigmoid'))
             # Adding in dictionary
             params['C'] = c_regular
             params['kernel'] = kernel_custom

        # Adding Parameters for KNN
        case "KNN":

            # Adding number of Neighbour in Classifier
            k_n = st.sidebar.slider('Number of Neighbors (K)', 1, 20)
            # Adding in dictionary
            params['K'] = k_n
            # Adding weights
            weights_custom = st.sidebar.selectbox('Weights', ('uniform', 'distance'))
            # Adding to dictionary
            params['weights'] = weights_custom

        # Adding Parameters for Naive Bayes
        # It doesn't have any paramter
        case 'Naive Bayes':

            st.sidebar.info("This is a simple Algorithm.It dosen't have Parmeters for Hypertuning.")

        # Adding Parameters for Decision Tree
        case 'Decision Tree':

            # Taking max_depth
            max_depth = st.sidebar.slider('Max Depth', 2, 17)
            # Adding criterion
            # mse is for regression- It is used in RandomForestRegressor
            # mse will give error in classifier so it is removed
            criterion = st.sidebar.selectbox('Criterion', ('gini', 'entropy', 'log_loss'))
            # Adding splitter
            splitter = st.sidebar.selectbox("Splitter",("best","random"))
            # Taking random state
            # Adding to dictionary
            params['max_depth'] = max_depth
            params['criterion'] = criterion
            params['splitter'] = splitter

            # Exception Handling using try except block
            # Because we are sending this input in algorithm model it will show error before any input is entered
            # For this we will do a default random state till the user enters any state and after that it will be updated
            try:
                random = st.sidebar.text_input("Enter Random State")
                params['random_state'] = int(random)
            except:
                params['random_state'] = 4567

        # Adding Parameters for Random Forest
        case "Random Forest":

            # Taking max_depth
            max_depth = st.sidebar.slider('Max Depth', 2, 17)
            # Adding number of estimators
            n_estimators = st.sidebar.slider('Number of Estimators', 1, 90)
            # Adding criterion
            # mse is for regression- It is used in RandomForestRegressor
            # mse will give error in classifier so it is removed
            criterion = st.sidebar.selectbox('Criterion', ('gini', 'entropy', 'log_loss'))
            # Adding to dictionary
            params['max_depth'] = max_depth
            params['n_estimators'] = n_estimators
            params['criterion'] = criterion

            # Exception Handling using try except block
            # Because we are sending this input in algorithm model it will show error before any input is entered
            # For this we will do a default random state till the user enters any state and after that it will be updated
            try:
                random = st.sidebar.text_input("Enter Random State")
                params['random_state'] = int(random)
            except:
                params['random_state'] = 4567

        # Adding Parameters for Linear Regression
        case "Linear Regression":

            # Taking fit_intercept
            fit_intercept=st.sidebar.selectbox("Fit Intercept",('True','False'))
            params['fit_intercept']=bool(fit_intercept)
            # Normalize does not work in linear regression
            # Taking n_jobs
            n_jobs=st.sidebar.selectbox("Number of Jobs",(None,-1))
            params['n_jobs']=n_jobs

        # Adding Parameters for Logistic Regression
        case default:

            # Adding regularization parameter from range 0.01 to 10.0
            c_regular = st.sidebar.slider('C (Regularization)', 0.01, 10.0)
            params['C']=c_regular
            # Taking fit_intercept
            fit_intercept = st.sidebar.selectbox("Fit Intercept", ('True', 'False'))
            params['fit_intercept'] = bool(fit_intercept)
            # Taking Penalty only l2 and None is supported
            penalty=st.sidebar.selectbox("Penalty",('l2',None))
            params['penalty'] = penalty
            # Taking n_jobs
            n_jobs = st.sidebar.selectbox("Number of Jobs", (None, -1))
            params['n_jobs'] = n_jobs

    return params

params = add_parameter(algorithm)

# Now we will build ML Model for this dataset and calculate accuracy for that
def model(data,algorithm,params):

    match algorithm:

        case 'KNN':
            return KNeighborsClassifier(n_neighbors=params['K'], weights=params['weights'])

        case 'SVM':
            return SVC(C=params['C'], kernel=params['kernel'])

        case 'Decision Tree':
            return DecisionTreeClassifier(
            criterion=params['criterion'],splitter=params['splitter'],
            random_state=params['random_state'])

        case 'Naive Bayes':
            return GaussianNB()

        case 'Random Forest':
            return RandomForestClassifier(n_estimators=params['n_estimators'],
            max_depth=params['max_depth'],
            criterion=params['criterion'],
            random_state=params['random_state']
        )

        case 'Linear Regression':
            return LinearRegression(fit_intercept=params['fit_intercept'],n_jobs=params['n_jobs'])

        case default:
            return LogisticRegression(fit_intercept=params['fit_intercept'],penalty=params['penalty'],C=params['C'],n_jobs=params['n_jobs'])

# Now we will write the dataset information
# Since diabetes is a regression dataset, it does not have classes
def info(data_name):

    if data_name != "Diabetes":
        st.write(f"## Classification {data_name} Dataset")
        st.write(f'Algorithm is : {algorithm}')

        # Printing shape of data
        st.write('Shape of Dataset is: ', X.shape)
        st.write('Number of classes: ', len(np.unique(Y)))
        # Making a dataframe to store target name and value

        df = pd.DataFrame({"Target Value" : list(np.unique(Y)),"Target Name" : data.target_names})
        # Display the DataFrame without index labels
        st.write('Values and Name of Classes')

        # Display the DataFrame as a Markdown table
        # To successfully run this we need to install tabulate
        st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)
        st.write("\n")

    else:

        st.write(f"## Regression {data_name} Dataset")
        st.write(f'Algorithm is : {algorithm}')

        # Printing shape of data
        st.write('Shape of Dataset is: ', X.shape)

# Calling function to print Dataset Information
info(data_name)

# Now selecting classifier
algo_model = model(data,algorithm,params)

# Now splitting into Testing and Training data
# It will split into 80 % training data and 20 % Testing data
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8)

# Training algorithm
algo_model.fit(x_train,y_train)

# Now we will find the predicted values
predict=algo_model.predict(x_test)

# Finding Accuracy
# Evaluating/Testing the model
if algorithm != 'Linear Regression':
    # For all algorithm we will find accuracy
    st.write("Training Accuracy is:",algo_model.score(x_train,y_train)*100)
    st.write("Testing Accuracy is:",accuracy_score(y_test,predict)*100)
else:
    # Checking for Error
    # Error is less as accuracy is more
    # For linear regression we will find error
    st.write("Mean Squared error is:",mean_squared_error(y_test,predict))
    st.write("Mean Absolute error is:",mean_absolute_error(y_test,predict))

# Plotting Dataset
# Since there are many dimensions, first we will do Principle Component analysis to do dimension reduction and then plot

pca=PCA(2)
X_pca=pca.fit_transform(X)

# Plotting
fig = plt.figure()

# Now while plotting we have to show target variables for datasets
# Now since diabetes is regression dataset it dosen't have target variables
# So we have to apply condition and plot the graph according to the dataset
# Seaborn is used as matplotlib does not display all label names

def choice(data_name):

    match data_name:

        # Plotting Regression Plot for dataset diabetes
        # Since this is a regression dataset we show regression line as well
        case "Diabetes":

            # PLotting the dataset
            plt.scatter(X[:, 0], Y, c=Y, cmap='viridis', alpha=0.8)
            # Plotting regression line
            plt.plot(x_test, predict, color="red")
            # Giving Title
            plt.title("Regression Plot of Dataset")
            # Giving Legends
            plt.legend(['Actual Values', 'Best Line or General formula'])
            # Showing the range of points using colorbar
            plt.colorbar()

        # Plotting for digits
        # Since this dataset has many classes/target values we can plot it using seaborn
        # Also viridis will be ignored here and it will plot by default according to its own settings
        # But we can set Color palette according to our requirements
        # We need not to give data argument else it gives error
        # Hue paramter is given to show target variables
        case "Digits":
            colors=['purple', 'green', 'yellow','red','black','cyan','pink','magenta','grey','teal']
            sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1],hue=Y,palette=sns.color_palette(colors),alpha=0.4)
            plt.legend(data.target_names,shadow=True)
            plt.title("Scatter Plot of Dataset With Target Classes")

        # We cannot give data directly we have to specify the values for x and y
        case default:
            colors = ['purple','green','yellow']
            sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1],hue=Y, palette=sns.color_palette(colors), alpha=0.4,)
            # Giving legend
            # If we try to show the class target name it will show in different color than the ones that are plotted
            plt.legend(shadow=True)
            # Giving Title
            plt.title("Scatter Plot of Dataset With Target Classes")

# Calling Function
choice(data_name)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
st.pyplot(fig)
