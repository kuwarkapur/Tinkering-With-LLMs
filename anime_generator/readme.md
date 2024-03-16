# AnimeGPT

This repository contains a Streamlit web application that utilizes the Google GenerativeAI API along with Streamlit to generate fictional anime stories based on user-provided images and prompts.

## Introduction

AnimeGPT is an interactive tool that harnesses the power of AI to create engaging anime stories. By providing an image and a prompt, users can embark on a creative journey to generate unique narratives surrounding the characters depicted in the image.

## Usage

To use the AnimeGPT application:

1. **Upload an Image**: Select an image of a character you want to base the story on. The supported image formats are JPG, JPEG, and PNG.

2. **Submit**: Click the "Let the magic happens" button to initiate the story generation process.

3. **Explore the Story**: After submission, the application will generate a hero name based on the provided image. The hero name will be displayed, and you can choose to continue the hero's journey by clicking the "Do you want to continue the hero's journey?" button.

4. **Generate the Story**: If you choose to continue the journey, the application will generate a narrative based on the hero's name and the provided prompt. The story will unfold, offering you a glimpse into the adventures of the character.

5. **Farewell**: If you decide not to continue the journey, or after viewing the generated story, the application will bid you farewell with a heartfelt message.

## Implementation Details

The application is built using Streamlit, a popular Python library for creating interactive web applications. It integrates with the Google GenerativeAI API to generate text-based content, specifically tailored for anime storytelling.

The core functionalities of the application include:

- Uploading and displaying images using Streamlit's file uploader and image display components.
- Utilizing the GenerativeAI API to generate hero names and anime story narratives based on user input.
- Managing user sessions and state using Streamlit's session state management features to maintain continuity in the storytelling experience.

## Dependencies

The following dependencies are required to run the AnimeGPT application:

- Streamlit
- PIL (Python Imaging Library)
- Google GenerativeAI Python SDK

Ensure that these dependencies are installed in your Python environment before running the application.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Google for providing access to the GenerativeAI API.
- Streamlit developers for creating an intuitive framework for building interactive web applications.

---

Feel free to contribute to this project by providing feedback, suggestions, or even contributing code enhancements. Let your imagination run wild with AnimeGPT! 🌟
