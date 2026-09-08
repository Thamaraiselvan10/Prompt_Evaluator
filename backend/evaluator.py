from .prompt_builder import build_evaluation_prompt
from .gemini_client import generate_response


def evaluate_prompt(user_prompt: str) -> str:

    evaluation_prompt = build_evaluation_prompt(user_prompt)

    result = generate_response(evaluation_prompt)

    return result