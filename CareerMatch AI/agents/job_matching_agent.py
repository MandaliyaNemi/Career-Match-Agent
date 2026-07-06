import time


def match_job(resume, job_description, client):


    prompt = f"""

Compare resume with job description.

Resume:

{resume}


Job Description:

{job_description}


Return:

- Match percentage
- Matching skills
- Missing skills
- Suggestions

"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


    except Exception:

        time.sleep(5)


        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )


        return response.text