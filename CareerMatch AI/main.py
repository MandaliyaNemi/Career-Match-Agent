from google import genai
from dotenv import load_dotenv
from google.genai.errors import ClientError, ServerError
import os
import time


# Load API key from .env
load_dotenv()


def get_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY missing in .env file")

    client = genai.Client(
        api_key=api_key
    )

    return client



def generate_response(client, prompt):

    models = [
        "gemini-2.5-flash-lite",
        "gemini-2.5-flash"
    ]


    for model in models:

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return response.text


        except ServerError as e:

            print("Server error:", e)

            time.sleep(5)
            continue


        except ClientError as e:

            error = str(e)

            print("Client error:", error)


            if "429" in error:

                return (
                    "Gemini API quota exceeded. "
                    "Please wait or create a new API key."
                )


            return f"Gemini API error: {error}"



        except Exception as e:

            return f"Unexpected error: {e}"



# Testing Gemini connection

if __name__ == "__main__":


    client = get_client()


    prompt = """
    Explain AI Resume + Job Matching Agent.
    Explain in simple words.
    """


    result = generate_response(
        client,
        prompt
    )


    print("\nGemini Response:\n")
    print(result)