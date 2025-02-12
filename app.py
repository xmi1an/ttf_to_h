import streamlit as st

# Load the app code from secrets
app_code = st.secrets["code"]["app_code"]

# Execute the app code
exec(app_code)
