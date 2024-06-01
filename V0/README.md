# Scratch idea
This script demonstrates the use of the CLIP model for real-time inference and displaying the cosine similarity between a text prompt and the image captured from a webcam. The similarity score and the prompt are overlaid on the video feed.

## Clone the repository:

```bash
git clone https://github.com/mayuras7685/Prom-raw.git
cd V0
```

## Install the required Python packages:

```python
pip install -r requirements.txt
```

## Demo


https://github.com/mayuras7685/Prom-raw/assets/88922616/8a6f732b-bb78-4dae-b3f9-9e8e1504bff6



## How It Works

1. **Initialization:**

- The Clip model is instantiated.
- A text prompt ("Giraffe in arctic") is embedded using the CLIP model.

2. **Render Function:**
- The render function calculates the cosine similarity between the embedded text prompt and the embeddings of the current frame from the webcam.
- The similarity score is scaled and displayed on the image.
- The text prompt is also displayed on the image.

3. Stream Initialization:

- The `inference.Stream` class is used to start capturing video from the webcam.
- The render function is called for each frame, updating the displayed similarity and prompt in real-time.

## Configuration
- Source: Change `source = 2` to the appropriate webcam index if necessary.
- Prompt: Modify the prompt variable to change the text prompt used for similarity comparison.
