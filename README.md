# ATS Resume Evaluator


The ATS Resume Evaluator is a web application designed to help job seekers improve their resumes by evaluating them against specific job descriptions. Leveraging AI-powered technology, this tool provides detailed feedback, including a match percentage, missing keywords, and a profile summary, to help users optimize their resumes for the competitive job market.


Features

Job Description Input: Users can paste the job description they are targeting.

-Resume Upload: Users can upload their resumes in PDF format.

-AI-Powered Evaluation: The application uses Google's Gemini Pro AI model to evaluate the resume based on the job description.

-Detailed Feedback: The tool provides a detailed report including match percentage, missing keywords, and a profile summary.


Installation

Clone the repository:

-git clone https://github.com/your-username/ats-resume-evaluator.git

-cd ats-resume-evaluator

Install the required dependencies:

-pip install -r requirements.txt

Set up environment variables:

-Create a .env file in the project root directory.

-Add your Google Generative AI API key to the .env file:

-GOOGLE_API_KEY=your_google_api_key

Run the application:

-streamlit run app.py

Usage

-Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).



Technologies Used

-Python: The core programming language for the application.

-Streamlit: Used for building the web interface.

-Google Generative AI (Gemini Pro): Provides the AI capabilities for resume evaluation.

-PyPDF2: Handles PDF file reading and text extraction.
