import streamlit as st
import io
from PIL import Image
from clarifai.client.model import Model
from clarifai.client.input import Inputs
import tempfile
import os

# Set page configuration
st.set_page_config(
    page_title="Gemma OCR Text Extractor",
    page_icon="📝",
    layout="wide"
)

# Add CSS for fixed footer and improved image display
st.markdown("""
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f0f2f6;
        padding: 1rem;
        text-align: center;
        font-size: 0.9rem;
        border-top: 1px solid #e0e0e0;
        color: black;
    }
    .footer a {
        color: #0066cc;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    /* Improve image display container */
    .stImage img {
        max-width: 100%;
        height: auto;
        object-fit: contain;
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_image(image_bytes):
    """Use Clarifai Gemini-3-4B model to extract text from an image"""
    try:
        # Create prompt for OCR
        prompt = "Extract all the text from this image, preserve formatting as much as possible."
        
        model_prediction = Model("https://clarifai.com/gcp/generate/models/gemma-3-4b-it").predict(
            inputs=[Inputs.get_multimodal_input(
                input_id="",
                image_bytes=image_bytes,
                raw_text=prompt
            )],
        )
        
        # Get the extracted text
        extracted_text = model_prediction.outputs[0].data.text.raw
        
        return extracted_text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def main():
    # Header
    st.title("📝 Gemma OCR")
    
    # Create two columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Upload Image")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp"])
        
        if uploaded_file is not None:
            # Display the uploaded image with improved quality
            image = Image.open(uploaded_file)
            
            # Display image metadata
            st.caption(f"Image size: {image.width} x {image.height} pixels")
            
            # Option to adjust display size
            use_full_width = st.checkbox("Use full column width for image", value=True)
            
            if use_full_width:
                # Use the full width of the column without specifying width
                st.image(image, caption="Uploaded Image", use_container_width=True)
            else:
                # Let user select a custom width
                display_width = st.slider("Adjust image display width", 
                                         min_value=200, 
                                         max_value=1000, 
                                         value=min(600, image.width),
                                         step=50)
                st.image(image, caption="Uploaded Image", width=display_width)
        
        extract_button = st.button("Extract Text")
    
    with col2:
        if uploaded_file is not None and extract_button:
            with st.spinner("Extracting text..."):
                # Get image bytes
                image_bytes = uploaded_file.getvalue()
                
                # Extract text from image
                extracted_text = extract_text_from_image(image_bytes)
                
                # Display the results
                st.header("Extracted Text:")
                st.markdown(extracted_text)

                
                # Add a download button for the extracted text
                text_file = io.StringIO()
                text_file.write(extracted_text)
                st.download_button(
                    label="Download Text",
                    data=text_file.getvalue(),
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )
    
    # Fixed Footer with black text and link to Clarifai model
    st.markdown(
        '<div class="footer">Built with <a href="https://clarifai.com/gcp/generate/models/gemma-3-4b-it" target="_blank">Gemma3-4B-it</a></div>', 
        unsafe_allow_html=True
    )

    # Add some space at the bottom to prevent content from being hidden behind the footer
    st.markdown("<br><br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()