from multiprocessing.sharedctypes import Value
import streamlit as st
import matplotlib.image as im
import models


st.title('Shaft Earthing System Analyzer')
st.write('')
current_model = models.load_current_model()
voltage_model = models.load_voltage_model()
current, voltage = st.columns(2)
system_status = "System status: :blue[operating normal]"
with current:
   uploaded_file = st.file_uploader("upload Current output",type = ['JPG','jpg','png','PNG','jpeg'],key = "1")

   if uploaded_file is not None:
      # To read file as bytes:
      bytes_data = uploaded_file.getvalue()
      image = im.imread(uploaded_file)
      file_name = uploaded_file.name
      models.extract_current(image,file_name)
      current_state = models.test_current(current_model)
      st.write('Results:')
      if current_state < 0.5:
         st.markdown("Status: :red[Unhealthy]")
         system_status = "System status: :red[Alarm! abnormal Current]"
      else:
         st.markdown(":blue[Status: Normal]")

   else:
      st.markdown(":blue[Status: No Current output]")

with voltage:
   uploaded_voltage_file = st.file_uploader("upload Voltage output",type = ['JPG','jpg','png','PNG','jpeg'], key = "2")

   if uploaded_voltage_file is not None:
      # To read file as bytes:
      bytes_data = uploaded_voltage_file.getvalue()
      image = im.imread(uploaded_voltage_file)
      file_name = uploaded_voltage_file.name
      models.extract_voltage(image,file_name)
      voltage_state = models.test_voltage(voltage_model)
      st.write('Results:')
      if voltage_state < 0.5:
         st.markdown("Status: :red[Unhealthy]")
         system_status = "System status: :red[Alarm! abnormal Voltage]"
      else:
         st.markdown(":blue[Status: Normal]")

   else:
      st.markdown(":blue[Status: No Voltage output]")
st.write("")
st.markdown(system_status)
