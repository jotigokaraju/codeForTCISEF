import os
import base64
from groq import Groq
from IPython.display import Image

"""
Insert Groq Description Here
"""
client = Groq(
    api_key=os.environ['GROQ_API_KEY'],
)

# Models
llava_model = 'llava-v1.5-7b-4096-preview'
llama31_model = 'llama-3.1-70b-versatile'


# Load image
image_path = 'temp_image/image.png'
Image(image_path)


# Encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Convert image to text using Groq LLaVA model
def image_to_text(client, model, base64_image, prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model=model
    )

    return chat_completion.choices[0].message.content


# Generate a short story based on the image description
def description_summarization(client, image_description):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Using the following image description, shorten it into only 1-3 words that would be most useful for a blind person if they only had those words to see the world in front of them.",
            },
            {
                "role": "user",
                "content": image_description,
            }
        ],
        model=llama31_model
    )

    return chat_completion.choices[0].message.content


prompt = "Describe this image in a way that would be helpful to a deafblind person."
base64_image = encode_image(image_path)
image_description = image_to_text(client, llava_model, base64_image, prompt)
print(image_description + "\n\n")
print(description_summarization(client, image_description))
# Delete temp image here?
