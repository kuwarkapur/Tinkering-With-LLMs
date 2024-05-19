import streamlit as st
import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from io import BytesIO
from src.utils import display_link_preview, display_file_preview, extract_text
from prompts import PROMPTS

# Function to summarize text
@st.cache_data
def summarize_text(corpus, prompt_type="pdf_document", max_words=300):
    prompt = PROMPTS[prompt_type].format(max_words=max_words)  # Format the prompt with max_words

    OLLAMA_ENDPOINT = "https://46ee-34-143-158-22.ngrok-free.app/api/generate"

    OLLAMA_PROMPT = f"{prompt}\n\n{corpus}"
    OLLAMA_DATA = {
        "model": "llama3",
        "prompt": OLLAMA_PROMPT,
        "stream": False
    }

    response = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)
    return response.json()['response']


# Function to create a PDF from text content
def create_pdf(summary_text):
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title = Paragraph("Summary Report", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Summary Content
    for line in summary_text.split('\n'):
        paragraph = Paragraph(line, styles['BodyText'])
        story.append(paragraph)
        story.append(Spacer(1, 12))

    doc.build(story)
    pdf_buffer.seek(0)
    return pdf_buffer

# Main function for the Streamlit app
def main():
    st.set_page_config(layout="wide", page_title="Summarize Anything")
    st.title("Summarize Anything")

    with st.sidebar:
        st.header("Controls")
        uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx", "txt", "csv", "epub", "mp4"])
        link = st.text_input("Or enter a URL for a YouTube video or article")
        max_length = st.slider("Maximum summary length", 50, 500, 300)
        # Clear cache button
        if st.button("🔃 Refresh"):
            st.cache_data.clear()
            
        # In the main function inside the sidebar
        content_type = st.selectbox("Choose Content Type", options=list(PROMPTS.keys()))  # Select prompt type

    
    # Maintain state for the last active input
    if "last_active_input" not in st.session_state:
        st.session_state.last_active_input = None

    if uploaded_file:
        st.session_state.last_active_input = 'file_uploader'
        link = ""
    elif link:
        st.session_state.last_active_input = 'link_input'
        uploaded_file = None

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
        if text:
            summarized_text = summarize_text(text,content_type,max_length)
            st.subheader("Summarized Content")

            # Display the summary in a scrollable container
            st.markdown(
                f"""
                <div style='height: 400px; overflow-y: auto; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #260A1D;'>
                    <h3>Summary</h3>
                    <p>{summarized_text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Option to download the summary as a PDF
            pdf_buffer = create_pdf(summarized_text)
            st.download_button(label="Download Summary as PDF",
                               data=pdf_buffer,
                               file_name="summary.pdf",
                               mime="application/pdf")

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
