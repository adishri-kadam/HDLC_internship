import streamlit as st
st.header("Welcome To BMI Calculator : ")
st.text_input("Enter your name : ")
st.text("Enter your Gender : ")
st.radio("Gender",("Male","Female"))
st.number_input("Enter your age : ")
st.text_input("Enter your address : ")
weight = st.number_input("Enter your weight (in kgs)")
status = st.radio("sect your height format: ",('cms', 'meters', 'feet'))
if (status == 'cms'):
    height = st.number_input('Enter your height :')
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        pass

elif (status == 'meters'):
    height = st.number_input('Enter your Height :')
    try:
        bmi = weight / (height ** 2)
    except:
       pass
else:
    height = st.number_input('Enter your Height :')
    # 1 meter = 3.28ft
    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
       pass
if (st.button('Calculate BMI')):
    st.text("Your BMI Index is {}.".format(bmi))
    if (bmi < 16):
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")