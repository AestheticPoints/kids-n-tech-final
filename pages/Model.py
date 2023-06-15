import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

@st.cache_resource  # Allow the model to be mutated and cached
def load_model():
    return tf.keras.models.load_model("model.tf")

# Load the model
loaded_model = load_model()

# Function to preprocess the image
def preprocess_image(image):
    # Convert the image to RGB color
    image = image.convert('RGB')
    # Resize the image to match the model's input shape
    resized_image = image.resize((256, 256))
    # Expand dimensions to match the model's input shape
    input_image = np.expand_dims(resized_image, axis=0)
    return input_image

# Class labels
class_labels = {
    0: "DVD Reader",
    1: "Keyboard",
    2: "Mouse",
    3: "Monitor"
}

# Function to make predictions
def predict_image(image, loaded_model):
    # Preprocess the image
    input_image = preprocess_image(image)
    # Make prediction using the loaded model
    predictions = loaded_model.predict(input_image)
    # Get the predicted class index
    predicted_class = np.argmax(predictions)
    # Get the predicted class label
    predicted_label = class_labels[predicted_class]
    # Return the predicted label
    return predicted_label

st.title("Image Classification Model")
# Add content for the Image Classification Model page here
    
# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
# Perform prediction if image is uploaded and "Predict" button is clicked
if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)
    # Check if image is valid
    if image is not None:
        # Display the uploaded image
        st.image(image, caption="Uploaded Image")
        # Button to trigger prediction
        if st.button("Predict"):
            # Perform prediction
            predicted_label = predict_image(image, loaded_model)
            # Display the predicted label
            st.write("Prediction:", predicted_label)
    else:
        st.write("Invalid Image")