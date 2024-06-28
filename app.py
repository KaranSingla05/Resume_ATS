import streamlit as st
import os
import PyPDF2
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to get response from Gemini Pro model
def get_gemini_response(input_text, jd_text):
    input_prompt = f"""
    Hey Act like a skilled or a very experienced ATS (Application Tracking System)
    with a deep understanding of tech field, software engineering, data science, data analyst and big data engineering. 
    Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide
    best assistance for improving the resumes. Assign the percentage matching based on JD and the missing
    keyword with high accuracy
    resume:{input_text}
    description:{jd_text}
    
    I want the response in one single string having the structure
    {{"JD Match":"%","Missing Keywords":[],"Profile Summary":""}}
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="ATS Resume Evaluator", layout="centered")

st.title("Application Tracking System")
st.write("Enhance your resume based on specific job descriptions with our AI-powered evaluation tool.")

st.markdown("### Step 1: Enter Job Description")
jd = st.text_area("Job Description", height=150, help="Paste the job description here.")

st.markdown("### Step 2: Upload Your Resume")
uploaded_file = st.file_uploader("Upload your resume in PDF format", type="pdf", help="Upload your resume in PDF format.")

st.markdown("### Step 3: Evaluate Your Resume")
if st.button("Submit"):
    if uploaded_file is not None and jd:
        with st.spinner('Processing...'):
            try:
                # Extract text from uploaded PDF
                resume_text = input_pdf_text(uploaded_file)

                # Get response from Gemini Pro model
                response_text = get_gemini_response(resume_text, jd)

                # Display response
                st.subheader("Resume Evaluation Result:")
                st.json(response_text)
            except PyPDF2.utils.PdfReadError:
                st.error("Error: Could not read the PDF file.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please upload a resume and provide a job description.")

st.markdown("### Instructions")
st.write("""
- **Step 1:** Copy and paste the job description in the provided text area.
- **Step 2:** Upload your resume in PDF format.
- **Step 3:** Click on 'Submit' to evaluate your resume.
- The AI will analyze your resume against the job description and provide feedback including match percentage, missing keywords, and a profile summary.
""")
