# AnythingSummarized

Welcome to AnythingSummarized - your go-to application for effortlessly summarizing any text content! 🚀

Note: This project is still in progress, and exciting new features will be added soon! Stay tuned. 🔜

## Features

1. File Upload: Seamlessly upload a wide range of file formats, including PDF, DOCX, TXT, CSV, EPUB, and MP4, to extract text for summarization. 📂
2. URL Input: Alternatively, simply provide a URL for a YouTube video or an article, and we'll handle the rest! 🌐
3. Text Summarization: Harness the power of the Ollama API to generate concise and informative summaries of the input text, capturing the core information and actionable insights. 🧠
4. Summarized Content Display: Enjoy a visually appealing and easy-to-read display of the summarized content, presented in a sleek, card-like container. 📰
5. Responsive UI: Experience a user-friendly and responsive interface, with a handy sidebar for controlling the input source (file or URL). 📱

## Upcoming Features

1. Optimized Architecture: Planned improvements to the application's architecture for enhanced performance and efficient summarization tasks. ⚡
2. Model Selection: The ability to choose from a variety of pre-trained language models within the web application to suit your specific summarization needs. 🔢
3. Q/A & Chat Functionality: Interactive question-answering sessions and natural language conversations with the summarized content. 💬
4. Multi-Format Support: Summarization of content in various formats, including text, audio, and video, for increased versatility. 📚📽️🎧

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/AnythingSummarized.git
2. Navigate to the project directory:

   ```bash
   cd AnythingSummarized
3. Install the required dependencies:
   ```bash
   cd requirements
   pip install -r requirements.txt

## Setup

1. Run the Ollama endpoint Jupyter Notebook first.
2. Replace the URL for the API request with the appropriate ngrok URL (e.g., https://3d34-34-87-154-37.ngrok-free.app).
3. In your command-line interface, set the OLLAMA_HOST environment variable:
   ```bash
   export OLLAMA_HOST=https://3d34-34-87-154-37.ngrok-free.app
4. Pull the desired Ollama model:
   ```bash
   ollama pull <model_name>

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py

2. The application will open in your default web browser.
3. In the sidebar, you can either upload a file or provide a URL for a YouTube video or an article.
4. After entering the input source, the application will display the original content and the summarized version in separate columns.
5. The summarized content will be presented in a visually appealing card-like container, making it easy to read and understand.

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## Contact
For any questions or feedback, feel free to reach out: [kuwarkapur@gmail.com](mailto:kuwarkapur@gmail.com).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
