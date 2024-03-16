import streamlit as st
import os
from PIL import Image
import google.generativeai as genai



genai.configure(api_key='AI************************************')

## Function to load OpenAI model and get respones

def get_gemini_response_name(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(image[0])
    return response.text

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Fictional Anime Generator")

st.header("AnimeGPT")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Let the magic happens")

input_prompt = """
               "Create an anime story around the hero name."

               Feel free to expand upon this prompt by developing the setting, supporting characters, conflicts, and resolution of the story. 
               Let your imagination soar as you craft an exciting narrative centered around the main character and his adventures!
               """

## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    name=get_gemini_response_name(image_data)
    st.session_state['hero_name'] = name  # Save the hero's name in session state
    st.subheader(f"The hero of the story is {name}")
    st.session_state['submitted'] = True  # Flag that the submit button has been pressed

if 'submitted' in st.session_state and st.session_state['submitted']:
    continue_journey = st.button("Do you want to continue the hero's journey?")
    image_data = input_image_setup(uploaded_file)
    if continue_journey:
        # Assuming get_gemini_response is a function defined elsewhere
        response = get_gemini_response(input_prompt, image_data, st.session_state['hero_name'])
        st.subheader("The story goes like this..")
        st.write(response)
        st.session_state['journey_continued'] = True  # Flag that the user chose to continue
    elif 'journey_continued' not in st.session_state:
        # Only show the farewell message if the user has seen and decided not to continue the journey
        st.subheader("If not then Until we meet again, may your journey be filled with safe travels and wondrous adventures. May the winds guide you gently, and the stars illuminate your path. Though we part ways for now, our memories will remain intertwined like the threads of fate, weaving a tapestry of friendship that transcends distance and time. Farewell, dear friend, until our paths converge once more.")


      
