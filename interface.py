from multiprocessing.sharedctypes import Value
import streamlit as st
import matplotlib.image as im
import models


st.title('Shaft Earthing System Analyzer')
st.write('')
current_model = models.load_current_model()
voltage_model = models.load_voltage_model()
uploaded_file = st.file_uploader("Choose system output",type = ['JPG','jpg','png','PNG','jpeg'])
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     image = im.imread(uploaded_file)
     file_name = uploaded_file.name
     models.extract_voltage(image,file_name)
     models.extract_current(image,file_name)
     voltage_state = models.test_voltage(voltage_model)
     current_state = models.test_current(current_model)
     st.write('Results:')
     if voltage_state < 0.5:
        st.write('Voltage: Unhleathy')
     else:
        st.write('Voltage: Normal')
     if current_state < 0.5:
        st.write('Current: Unhealthy')
     else:
        st.write('Current: Normal')