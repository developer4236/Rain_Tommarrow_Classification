import streamlit as st
import numpy as np
import pickle



# Load the dataset and model
df = pickle.load(open('clean_data.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



# Select the cat_values
WindGustDir = df['WindGustDir'].unique().tolist()
WindGustDir.insert(0,'Select ')
WindDir9am = df['WindDir9am'].unique().tolist()
WindDir9am.insert(0,'Select ')
WindDir3pm = df['WindDir3pm'].unique().tolist()
WindDir3pm.insert(0,'Select ')



#Title of the site
st.title('Rain Tommarow Prediction')



# All Columns manage
# Three Columns
col1, col2, col3= st.columns(3)
with col1:
    windgust_dir = st.selectbox('WindGustDir',WindGustDir)
with col2:
    winddir_9am = st.selectbox('WindDir9am',WindDir9am)
with col3:
    winddir_3pm = st.selectbox('WindDir3pm',WindDir3pm)


# Three Columns
col1, col2, col3= st.columns(3)
with col1:
    windgust_speed = st.text_input('WindGustSpeed')
with col2:
    windspeed_9am = st.text_input('WindSpeed9am')
with col3:
    windspeed_3pm = st.text_input('WindSpeed3pm')


# Two Columns
col1, col2= st.columns(2)
with col1:
    min_tem = st.text_input('MinTemp')
with col2:
    max_temp = st.text_input('MaxTemp')


# Two Colums
col1, col2= st.columns(2)
with col1:
    humidity_9am = st.text_input('Humidity9am')
with col2:
    humidity_3pm = st.text_input('Humidity3pm')


# Two Columns
col1, col2= st.columns(2)
with col1:
    pressure_9am = st.text_input('Pressure9am')
with col2:
    pressure_3pm = st.text_input('Pressure3pm')


# Two Columns
col1, col2= st.columns(2)
with col1:
    temp_9am = st.text_input('Temp9am')
with col2:
    temp_3pm = st.text_input('Temp3pm')


# Two Columns
col1, col2= st.columns(2)
with col1:
    rain_fall = st.text_input('Rainfall')
with col2:
    risk_mm = st.text_input('RISK_MM')



# All Data in one variable
selected_data = (min_tem,max_temp,rain_fall,windgust_dir,windgust_speed,winddir_9am,winddir_3pm,windspeed_9am,windspeed_3pm,humidity_9am,
                 humidity_3pm,pressure_9am,pressure_3pm,temp_9am,temp_3pm,risk_mm)


# Final Prediction
try:
    if st.button('Predict'):
        reshaped_data = np.asarray(selected_data).reshape(1,-1)
        if 'select' in reshaped_data or '' in reshaped_data:
            st.warning('Please fill all values')
        else:
            prediction = model.predict(reshaped_data)
            if prediction[0] == 0:
                st.warning("it won't rain tomorrow")
            else:
                st.success("It will be rainy tomorrow")
except Exception as e:
    st.warning(f'An error occurred: {e}')


