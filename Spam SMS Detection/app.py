# you can run your app with: streamlit run app.py

import streamlit as st
import pickle

# loading trained model

model = pickle.load(open('model.pkl', 'rb')) # read in binary mode

# create title
st.title('SMS Spam Classifier')

message = st.text_input('Enter any message:')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])
    print(prediction)
    st.write(prediction)
    if prediction[0] == 'spam':
        st.warning('This message is a spam message :(')
    else:
        st.success('This message is a legit message :)')