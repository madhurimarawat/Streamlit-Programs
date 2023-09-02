# Trying to build a simple app with streamlit
# Streamlit is a python framework through which we can deploy any machine learning model and any python project with ease and without worrying about the frontend.
# Streamlit is very user-friendly.
# With the following command we can run streamlit app
# streamlit run filename.py
# We can change our file while our localhost is running and it will reflect changes
# Also we can run Multiple Files at the same time in the localhost also

# Importing Module
import streamlit as st

# For title we use st.title method
st.title("Basic App in Python Using Streamlit!!")

# Giving Header and Subheader to our App

# For Header
st.header("This is a Header")

# For Subheader
st.subheader("This is a Subheader")

# For writing Text we use text function
st.text("Hello Everyone!!!")

# Markdown option is also available
# # For h1 heading tag and it takes upto six #
st.markdown("# This is a Markdown Header 1")
st.markdown("## This is a Markdown Header 2")
st.markdown("### This is a Markdown Header 3")

# It also has inbuilt functions for showing Warning and Exceptions

# For displaying Success Message- Shows in Green
st.success("For Showing Successful Submission")

# For showing Information- Shows in Blue
st.info("Information")

# For showing Warning- Shows in Yellow
st.warning("This is a Warning")

# For showing Error- Shows in Red
st.error("Error Encountered!!")

# For showing Exception- Shows in Red
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write - Displays Code in Coding Format
st.write("Writing Python Inbuilt Range Function")
st.write(range(10))

# We can also display images using Pillow
# Displaying Images
# import Image from pillow to open images
from PIL import Image

# Here we have loaded the image in the img variable
img=Image.open("Picture-1.jpg")

# Width is used to set the width of an image
st.image(img, width=200)

# Checkbox- A checkbox returns a boolean value.
# When the box is checked, it returns a True value else returns a False value.
# Checking if the checkbox is checked
# Title of the checkbox is 'Show/Hide'

if st.checkbox("Show/Hide"):
 
    # Display the text if the checkbox returns True value
    st.text("Showing the widget")

# Radio Button
# First argument is the title of the radio button
# Second argument is the options for the radio button

status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# Conditional statement to print
# Male if male is selected else print female
# Showing the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

# Selection Box
# We can select any one option from the select box

# First argument takes the titleof the selectionbox
# Second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# Print the selected hobby
st.write("Your hobby is: ", hobby)

# Multi-Selectbox
# The multi-select box returns the output in the form of a list. 
# We can select multiple options

# First argument takes the titleof the selectionbox
# Second argument takes options
prog_lang = st.multiselect("Programming Languages: ",
                     ['C', 'C++',"PHP", 'Python','R',"Ruby"])
 
# Print the selected Programming Languages
st.write("Programming Languages you selected are: ", len(prog_lang),'prog_lang')

# Creating a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To My App!!!")

# Text Input
# Save the input text in the variable 'name'
# First argument shows the title of the text input box
# Second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")
 
# Display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)

# Slider
# First Argument is the title of the Slider
# Second Argument takes starting of the Slider
# Last Argument shows ending of the Slider 

level=st.slider("Select The Level",1,5)

# Printing Level
# Format is used to print value of variable at specific position
st.text("Selected: {}".format(level))