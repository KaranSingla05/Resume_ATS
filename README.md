# ATS Resume Evaluator

The ATS Resume Evaluator is a web application designed to help job seekers improve their resumes by evaluating them against specific job descriptions. Leveraging AI-powered technology, this tool provides detailed feedback, including a match percentage, missing keywords, and a profile summary, to help users optimize their resumes for the competitive job market.

## Features

- **Job Description Input**: Users can paste the job description they are targeting.
- **Resume Upload**: Users can upload their resumes in PDF format.
- **AI-Powered Evaluation**: The application uses Google's Gemini Pro AI model to evaluate the resume based on the job description.
- **Detailed Feedback**: The tool provides a detailed report including match percentage, missing keywords, and a profile summary.

## How It Works

1. **Step 1: Enter Job Description**
   - Copy and paste the job description into the provided text area.

2. **Step 2: Upload Your Resume**
   - Upload your resume in PDF format using the file uploader.

3. **Step 3: Evaluate Your Resume**
   - Click on the 'Submit' button to start the evaluation process.
   - The AI will analyze your resume against the job description and provide feedback.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ats-resume-evaluator.git
    cd ats-resume-evaluator
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the project root directory.
    - Add your Google Generative AI API key to the `.env` file:
        ```
        GOOGLE_API_KEY=your_google_api_key
        ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage

- Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
- Follow the steps to input the job description, upload your resume, and receive feedback.

## Technologies Used

- **Python**: The core programming language for the application.
- **Streamlit**: Used for building the web interface.
- **Google Generative AI (Gemini Pro)**: Provides the AI capabilities for resume evaluation.
- **PyPDF2**: Handles PDF file reading and text extraction.
- **dotenv**: Manages environment variables.
