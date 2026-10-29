import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/'

st.title('Gotu AI: The Intelligent Friend of Farmers.')


try:
    response = requests.get(API_URL)

    if response.status_code == 200:
        st.write(f'API connected successfully with status code: {response.status_code}')
        st.success(response.json()['message'])


    else: st.error(f'API return some error with status code: {response.status_code}')

except requests.exceptions.ConnectionError:
    st.error('API not connected please check the backend system!!!')
