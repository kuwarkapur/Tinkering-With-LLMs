import streamlit as st
import requests
from src.utils import display_link_preview,display_file_preview,extract_text


def summarize_text(corpus):
    

     prompt = """Objective: Summarize the provided text in about 300 words, focusing on the core information and actionable insights.
            use bullets or headings wherever needed,
            Instructions:

            Key Points Identification:
            List the main themes and important messages.
            Summary Creation:
            Construct a summary under appropriate headings reflecting the text's structure.
            Action Items:
            Clearly list any recommendations or steps to be taken as highlighted in the text.
            Editing:
            Ensure the summary is clear and concise, within the specified word count.
            Format:

            Use headings to organize the summary into sections.
            Keep each section focused and succinct."""

     OLLAMA_ENDPOINT = "https://3d34-34-87-154-37.ngrok-free.app/api/generate"

     OLLAMA_PROMPT = f"{prompt}: {corpus}"
     OLLAMA_DATA = {
          "model": "llama3",
          "prompt": OLLAMA_PROMPT,
          "stream": False
     }

     response = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)
     return response.json()['response']

# Main function for the Streamlit app
def main():
    st.set_page_config(layout="wide", page_title="summarise anything")
    st.title("summarise anything")
    with st.sidebar:
        st.header("Controls")
        uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx", "txt", "csv", "epub", "mp4"])
        link = st.text_input("Or enter a URL for a YouTube video or article")
        
    if st.session_state.get("file_uploader") and st.session_state.get("link_input"):
        # If both inputs are filled, clear the one not currently being modified
        if st.session_state.last_active_input == 'file_uploader':
            st.session_state.link_input = ""
        else:
            st.session_state.file_uploader = None


    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("Original Content")
        if uploaded_file:
            display_file_preview(uploaded_file)
            text = extract_text(uploaded_file)
        elif link:
            display_link_preview(link)
            text = extract_text(link)
        else:
            text = ""

    with col2:
        
        summarized_text = summarize_text(text)
    
        st.subheader("Summarized Content")
        # Example of displaying a card-like container for summaries
        st.container().markdown(
            summarized_text, unsafe_allow_html=True)

    st.markdown("""
        <style>
        /* Add custom styles here */
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            border: 1px solid rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
