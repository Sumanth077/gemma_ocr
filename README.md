# Gemma OCR

A Streamlit application that extracts text from images using Google's Gemma 3-4B model via Clarifai.

## Features

- Upload images in various formats (JPG, JPEG, PNG, BMP)
- Extract text from images using Gemma 3-4B model
- Download extracted text as a file
- Responsive UI with image display options

## Requirements

- Python 3.7+
- Streamlit
- Pillow
- Clarifai

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install streamlit pillow clarifai
   ```
3. Set your Clarifai PAT (Personal Access Token) as an environment variable:
   ```
   export CLARIFAI_PAT="your_clarifai_pat"
   ```
4. Run the application:
   ```
   streamlit run ocr_app/app.py
   ```

## Usage

1. Upload an image containing text
2. Click "Extract Text"
3. View the extracted text
4. Download the text if needed