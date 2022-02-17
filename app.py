import streamlit as st
import pandas as pd
import numpy as np
import time



#Initialize web app with simple table and comment

st.write("Here's our first attempt at using data at create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

# Line Charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

# Widgets
x = st.slider('x')
st.write(x, 'Squared is', x * x)

# Text input
st.text_input("Your name", key='name')

# Check box
if st.checkbox("Output session name"):
    st.session_state.name
    
if st.checkbox("Output line chart"):
    st.line_chart(chart_data)
    
# Selectbox

option = st.selectbox("Which option do you want", df['first column'])

# Sidebar

option_sidebar = st.sidebar.selectbox("How would you like to be contacted", ('Email', 'Phone'))
add_slider = st.sidebar.slider("Select a range of values", 0, 100, (25, 75))

# Progress bar


#Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    #update the progress bar with each iteration
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
    
    

