import streamlit as st
import pandas as pd
import numpy as np
import time
st.set_page_config(initial_sidebar_state='auto')

    
#Initialize web app with simple table and comment

st.write("Number of participant")
df = pd.DataFrame({
    'Name': ['Arvin', 'Mac', 'Lee', 'Nao'],
    'Location': ['4A', '4B', '4A', '4B']
})

option_sidebar = st.sidebar.selectbox("Would you like to show Data?", ('No', 'Yes'))
if option_sidebar == "Yes":
    st.write(df)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Meron', 'Wala', 'Draw']
)
st.line_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(chart_data)

# Caching

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")