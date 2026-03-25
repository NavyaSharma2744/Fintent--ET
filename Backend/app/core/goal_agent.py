from app.services.llm_service import extract_goals

def process_goals(user_input: str):
    result = extract_goals(user_input)

    try:
        goals = result.choices[0].message.function_call.arguments
        return goals
    except:
        return {"goals": []}