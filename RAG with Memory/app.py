import streamlit as st
from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain,LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_general_chain(question):
    
    prompt_template = "I want to know about so please Answer as detailed as possible from your knowledge"
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt_template,question])

    return response.text


def get_conversational_chain(vectordb):

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3,convert_system_message_to_human=True)

    # prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    retriever = vectordb.as_retriever()
    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(prompt_template)

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True, output_key='answer')

    conversation_chain = (ConversationalRetrievalChain.from_llm
                          (llm=model,
                           retriever=retriever,
                           condense_question_prompt=CONDENSE_QUESTION_PROMPT,
                           memory=memory,
                           return_source_documents=True))
    print("Conversational Chain created for the LLM using the vector store")
    return conversation_chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)

    chain = get_conversational_chain(new_db)

    
    response = chain(user_question)
    return response['answer']




def main():
    
                
    if "history" not in st.session_state:
        st.session_state.history = []
        
    st.set_page_config("Chatting with Cheatsheets")
    st.header("Chat with PDF using Gemini💁")
    # Initialize chat session in Streamlit if not already present
    
    
    for msg in st.session_state.history:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])


    user_question = st.chat_input("Ask a Question from the PDF Files")

    if user_question:
        
        st.session_state.history.append({
        'role':'user',
        'content':user_question
         })

        
        # Add user's message to chat and display it
        st.chat_message("user").markdown(user_question)

        # Send user's message to Gemini-Pro and get the response
        gemini_response = user_input(user_question)
        
        if "does not" in gemini_response.lower() or "cannot answer" in gemini_response.lower() or "sorry" in gemini_response.lower():
            gemini_response_general=get_general_chain(user_question)

            # Display Gemini-Pro's response
            with st.chat_message("assistant"):
                st.markdown(gemini_response)
                st.markdown("but here is what i know on the context")
                st.markdown(gemini_response_general)
                
        else:
            st.session_state.history.append({
                'role' : 'Assistant',
                'content' : gemini_response
            })

            # Display Gemini-Pro's response
            with st.chat_message("assistant"):
                st.markdown(gemini_response)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        pdf_docs=list(pdf_docs)
        print(pdf_docs)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()