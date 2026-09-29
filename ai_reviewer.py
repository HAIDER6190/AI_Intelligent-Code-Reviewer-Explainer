import os
import json

from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")


client = genai.Client(api_key=API_KEY)


def review_code(code: str, language: str) -> str:
    """Send source code to Gemini and return the code review."""

    user_prompt = (
        "Programming Language: "
        + language
        + "\n\nSource Code:\n"
        + "```"
        + language
        + "\n"
        + code
        + "\n```"
    )

    prompt = SYSTEM_PROMPT + "\n\n" + user_prompt

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )

    return json.loads(interaction.output_text)