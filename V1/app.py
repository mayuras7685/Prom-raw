import streamlit as st
import clip
import torch
import plotly.graph_objs as go
from PIL import Image
import numpy as np
import math
from itertools import chain

device = "cuda" if torch.cuda.is_available() else "cpu"

# Function to load CLIP model
@st.cache_resource()
def load_clip_model():
    return clip.load("ViT-B/32", device=device)

# Function to handle text prompt input
def input_text():
    prompt = st.text_input("Enter text prompt")
    return prompt

# Function to handle image addition
def add_images():
    uploaded_images = st.file_uploader("Upload images", accept_multiple_files=True)
    images = [Image.open(image) for image in uploaded_images]
    image_names = [image.name for image in uploaded_images]
    return images, image_names

# Function to display images in a grid layout
def display_image_grid(images, image_names, columns=3):
    c = len(images)
    r = math.ceil(c / columns)
    for i in range(r):
        col1, col2, col3 = st.columns(columns)
        for j in range(columns):
            index = i * columns + j
            if index < c:
                getattr(eval(f'col{j+1}'), 'image')(images[index], caption=image_names[index], use_column_width=True)

# Load CLIP model
model, transform = load_clip_model()


title_writing = "🎨Promraw"
title_format = f'<p style="text-align: center; font-family: ' \
               f'sans-serif; color: #ff0f7b; font-size: 50px; ' \
               f'font-weight: 700;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

# Get text prompt
prompt = input_text()

# Get uploaded images
images, image_names = add_images()

# Display uploaded images in a grid layout
if images:
    st.subheader("Uploaded Images")
    display_image_grid(images, image_names)

# Button to compute similarity
if st.button("Compute Similarity"):
    if prompt and images:
        # Convert images to tensors and move to appropriate device
        images_tensor = torch.stack([transform(image).to(device) for image in images])

        # Tokenize prompt
        text = clip.tokenize([prompt]).to(device)

        # Compute embeddings
        image_features = model.encode_image(images_tensor)
        text_features = model.encode_text(text)

        # Calculate similarity scores and convert to percentages
        similarity_scores = (text_features @ image_features.T).softmax(dim=1)
        percentage_list = [[value.item() * 100 for value in row] for row in similarity_scores]
        scores = list(chain(*percentage_list))

        # Plot similarity scores
        fig = go.Figure()
        fig.add_trace(go.Bar(x=image_names, y=scores, marker_color='lightsalmon'))
        fig.update_layout(title="Similarity Scores", xaxis_title="Image", yaxis_title="Similarity Score (%)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please enter a text prompt and upload images before computing similarity.")

# # Button to compute similarity
# if st.button("Compute Similarity"):
#     if prompt and images:
#         # Convert images to tensors and move to appropriate device
#         images_tensor = torch.stack([transform(image).to(device) for image in images])

#         # Tokenize prompt
#         text = clip.tokenize([prompt]).to(device)

#         # Compute embeddings
#         image_features = model.encode_image(images_tensor)
#         text_features = model.encode_text(text)

#         # Calculate similarity scores and convert to percentages
#         similarity_scores = (text_features @ image_features.T).softmax(dim=1)
#         percentage_list = [[value.item() * 100 for value in row] for row in similarity_scores]
#         scores = list(chain(*percentage_list))

#         # Plot similarity scores using indicator
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number+delta",
#             value=scores[0],  # Displaying score of the first image only
#             domain={'x': [0, 1], 'y': [0, 1]},
#             title={'text': "Similarity Score (%)", 'font': {'size': 24}},
#             gauge={
#                 'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "black"},
#                 'bar': {'color': "#0057e7"},
#                 'bgcolor': "white",
#                 'borderwidth': 2,
#                 'bordercolor': "gray",
#                 'steps': [
#                     {'range': [0, 20], 'color': '#d62d20'},
#                     {'range': [20, 80], 'color': '#ffa700'},
#                     {'range': [80, 100], 'color': '#008744'}
#                 ],
#                 'threshold': {
#                     'line': {'color': "#000000", 'width': 4},
#                     'thickness': 0.75,
#                     'value': 90  # Adjust threshold value as needed
#                 }
#             }
#         ))
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Please enter a text prompt and upload images before computing similarity.")
