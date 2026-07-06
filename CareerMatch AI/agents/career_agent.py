def career_suggestion(resume_analysis, client):


    prompt = f"""

You are a Career Guidance AI Agent.

Based on this resume analysis:

{resume_analysis}


Suggest:

1. Career path
2. Skills to learn
3. Projects to build
4. Resume improvements
5. Interview preparation tips


"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


    return response.text