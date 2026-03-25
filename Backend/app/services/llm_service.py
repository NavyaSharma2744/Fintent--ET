from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_goals(user_input: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract financial goals and classify into short-term or long-term."},
            {"role": "user", "content": user_input}
        ],
        functions=[
            {
                "name": "save_goals",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "goals": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "type": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            }
        ],
        function_call="auto"
    )

    return response