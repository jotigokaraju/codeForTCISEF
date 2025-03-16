import streamlit as st
from transformers import pipeline
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Load the pipeline outside Streamlit script
caption = None

@st.cache_resource
def load_processor():
    return TrOCRProcessor.from_pretrained('microsoft/trocr-base-str')

@st.cache(allow_output_mutation=True)
def load_model():
    VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-str')



# Streamlit script
def main():
    global caption
    if caption is None:
        model = load_model()
        processor = load_processor()

    photo = st.camera_input("Take a picture")
    if photo is not None:
        image = Image.open(photo).convert("RGB")
        st.image(Image.open(photo))

    if st.button("Caption") and image is not None:
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        st.write(generated_text)

if __name__ == "__main__":
    main()
