import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import removebg

# display an upload file dialog for the user to select an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png"])

# check if the user has uploaded an image
if uploaded_file is not None:

    # read the contents of the image file
    img = Image.open(uploaded_file)

    # create a buffer to hold the image data
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")

    # remove the background of the image using the remove.bg API
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': img_buffer.getvalue()},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'YOUR_API_KEY'},
    )

    # convert the response to a PIL image
    output_img = Image.open(BytesIO(response.content))

    # display the image with the background removed
    st.image(output_img, caption="Image with Background Removed", use_column_width=True)
