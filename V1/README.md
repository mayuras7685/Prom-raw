# Promraw: Image-Text Similarity Application

Streamlit-based application that allows users to compute similarity scores between a text prompt and a set of uploaded images using the CLIP (Contrastive Language-Image Pretraining) model. The application provides a user-friendly interface for uploading images, entering a text prompt, and visualizing the similarity scores.

![image](https://github.com/mayuras7685/Prom-raw/assets/88922616/16edbc5a-a84c-4b37-896e-fb3338d7f661)

## Features

1. **Text Prompt Input**: Allows users to input a text prompt.
2. **Image Upload**: Users can upload multiple images.
3. **Image Display**: Displays the uploaded images in a grid layout.
4. **Compute Similarity**: Calculates similarity scores between the text prompt and uploaded images.
5. **Plot Similarity Scores**: Visualizes the similarity scores as a bar chart using Plotly.

## How to Use

1. **Launch the Application**: Run the Streamlit app to open the Promraw interface.
2. **Enter Text Prompt**: Input a descriptive text prompt in the provided text box.
3. **Upload Images**: Use the file uploader to select and upload multiple images.
4. **Display Images**: The uploaded images are displayed in a grid layout for easy viewing.
5. **Compute Similarity**: Click the "Compute Similarity" button to generate similarity scores between the text prompt and each uploaded image.
6. **View Results**: The similarity scores are displayed as a bar chart, showing the percentage similarity for each image.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mayuras7685/Prom-raw.git
   cd V1
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Code Explanation

### Load CLIP Model
```python
@st.cache_resource()
def load_clip_model():
    return clip.load("ViT-B/32", device=device)
```
This function loads the CLIP model and caches it to improve performance by avoiding reloading the model multiple times.

### Input Text
```python
def input_text():
    prompt = st.text_input("Enter text prompt")
    return prompt
```
This function creates a text input box for the user to enter the text prompt.

### Add Images
```python
def add_images():
    uploaded_images = st.file_uploader("Upload images", accept_multiple_files=True)
    images = [Image.open(image) for image in uploaded_images]
    image_names = [image.name for image in uploaded_images]
    return images, image_names
```
This function handles image uploads, opens the images, and returns them along with their file names.

### Display Image Grid
```python
def display_image_grid(images, image_names, columns=3):
    c = len(images)
    r = math.ceil(c / columns)
    for i in range(r):
        col1, col2, col3 = st.columns(columns)
        for j in range(columns):
            index = i * columns + j
            if index < c:
                getattr(eval(f'col{j+1}'), 'image')(images[index], caption=image_names[index], use_column_width=True)
```
This function displays the uploaded images in a grid layout using Streamlit's column feature.

### Compute Similarity and Display Results
```python
if st.button("Compute Similarity"):
    if prompt and images:
        images_tensor = torch.stack([transform(image).to(device) for image in images])
        text = clip.tokenize([prompt]).to(device)
        image_features = model.encode_image(images_tensor)
        text_features = model.encode_text(text)
        similarity_scores = (text_features @ image_features.T).softmax(dim=1)
        percentage_list = [[value.item() * 100 for value in row] for row in similarity_scores]
        scores = list(chain(*percentage_list))

        fig = go.Figure()
        fig.add_trace(go.Bar(x=image_names, y=scores, marker_color='lightsalmon'))
        fig.update_layout(title="Similarity Scores", xaxis_title="Image", yaxis_title="Similarity Score (%)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please enter a text prompt and upload images before computing similarity.")
```
This section includes the logic for computing similarity scores, converting them to percentages, and displaying the results as a bar chart.
