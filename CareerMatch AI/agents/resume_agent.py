from pypdf import PdfReader
import time


def extract_resume_text(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text



def analyze_resume(resume_text, client):

    prompt = f"""

You are a Resume Analyzer AI Agent.

Analyze this resume:

{resume_text}

Give:

1. Skills
2. Education
3. Experience
4. Strengths
5. Weaknesses
6. Missing skills

"""


    models = [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
    ]


    for model in models:

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text


        except Exception as e:

            print(
                f"{model} failed: {e}"
            )

            time.sleep(5)



    return "Gemini server unavailable. Try again after some time."