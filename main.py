import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
from streamlit_extras.switch_page_button import switch_page


st.title("Welcome to Kids-N-Tech")

st.markdown("I am from Haiti. The first time I saw a computer, I was 14 years old. However, little did I know that my first experience with a computer would set me on a path, changing my life forever and empowering me to, one day, bridge the digital divide in my country and provide world-class opportunities to millions.")

st.markdown("Over the past four years, I embarked on a journey as a computer lab coordinator with the goal of building computer labs in Haiti's rural areas.")

st.markdown("During this journey, I observed two major challenges:")

st.markdown("1. An average of 90% of rural kids have no idea about computer basics and the internet.")

st.markdown("2. A lack of on-the-ground experts to support the kids and answer their questions.")

st.markdown("To address these challenges, I came to Montreal and explained the obstacles I was facing to my team. Thanks to their support, we have introduced 'Kids-n-tech,' an app that allows kids to learn about computer components through images without the need for on-the-ground experts.")

st.markdown("Our aim is to provide an accessible platform for children to learn and understand computer technology, enabling them to acquire valuable skills and bridge the digital divide in rural areas.")

st.markdown("By utilizing this app, we aspire to empower the younger generation in Haiti and provide them with the tools and knowledge necessary to thrive in the digital age.")

st.markdown("Let's embark on this journey together and make a difference!")

st.markdown("---")

col1, col2 = st.columns(2)

# First button
if col1.button("Click here to start the quiz"):
    switch_page("Quiz")       

# Second button
if col2.button("Click here for prediction"):
    switch_page("Model")