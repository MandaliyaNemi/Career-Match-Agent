import streamlit as st
import os

from dotenv import load_dotenv
from google import genai


from agents.resume_agent import (
    extract_resume_text,
    analyze_resume
)

from agents.job_matching_agent import (
    match_job
)

from agents.career_agent import (
    career_suggestion
)



# Load API

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)


client = genai.Client(
    api_key=api_key
)



# UI Design

st.set_page_config(
    page_title="AI Resume Job Matcher",
    page_icon="🤖"
)


st.title(
    "🤖 AI Resume + Job Matching Agent"
)


st.write(
    "Upload your resume and get AI based job matching and career guidance"
)



# Upload Resume

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)



# Job Description

job_description = st.text_area(
    "Paste Job Description"
)



if st.button("Analyze Resume 🚀"):


    if uploaded_file is None:

        st.warning(
            "Please upload resume"
        )


    elif job_description == "":

        st.warning(
            "Please enter job description"
        )


    else:


        # Save uploaded file

        file_path = "resume.pdf"


        with open(file_path,"wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )



        with st.spinner(
            "Analyzing Resume..."
        ):


            resume_text = extract_resume_text(
                file_path
            )



            resume_analysis = analyze_resume(
                resume_text,
                client
            )



        st.subheader(
            "📄 Resume Analysis"
        )

        st.write(
            resume_analysis
        )



        with st.spinner(
            "Matching Job..."
        ):


            match_result = match_job(
                resume_text,
                job_description,
                client
            )


        st.subheader(
            "🎯 Job Matching Result"
        )


        st.write(
            match_result
        )



        with st.spinner(
            "Generating Career Advice..."
        ):


            career_result = career_suggestion(
                resume_analysis,
                client
            )



        st.subheader(
            "🚀 Career Suggestions"
        )


        st.write(
            career_result
        )