# Gemma OCR

A Streamlit application that extracts text from images using Google's [**Gemma 3-4B**](https://clarifai.com/gcp/generate/models/gemma-3-4b-it) model via Clarifai.

## Features

- Upload images in various formats (JPG, JPEG, PNG, BMP)
- Extract text from images using the **Gemma 3-4B** model
- Download extracted text as a file
- Responsive UI with image preview

## Requirements

- Python 3.10+
- Streamlit
- Pillow
- Clarifai SDK

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Sumanth077/gemma_ocr
   cd gemma_ocr
   ```

2. Install the dependencies:
   ```bash
   pip install streamlit pillow clarifai
   ```

3. Set your Clarifai Personal Access Token (PAT) as an environment variable:
   ```bash
   export CLARIFAI_PAT="your_clarifai_pat"
   ```

4. Run the application:
   ```bash
   streamlit run ocr_app/app.py
   ```