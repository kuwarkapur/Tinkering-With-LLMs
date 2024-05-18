# AnythingSummarized

This project is a Streamlit application that allows users to summarize any text content, whether it's from an uploaded file or a provided URL. The application utilizes the Ollama API to generate concise and informative summaries of the input text.

**Note: This project is still in progress, and features will be updated periodically.**

## Features

- **File Upload**: Users can upload various file formats such as PDF, DOCX, TXT, CSV, EPUB, and MP4 to extract text for summarization.
- **URL Input**: Alternatively, users can provide a URL for a YouTube video or an article, and the application will fetch and summarize the text content.
- **Text Summarization**: The application leverages the Ollama API to generate a summary of the input text, focusing on the core information and actionable insights.
- **Summarized Content Display**: The summarized content is displayed in a visually appealing card-like container, making it easy to read and understand.
- **Responsive UI**: The Streamlit application features a responsive and user-friendly interface, with a sidebar for controlling the input source (file or URL).

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
