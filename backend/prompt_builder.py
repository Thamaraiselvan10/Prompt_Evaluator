def build_evaluation_prompt(user_prompt: str) -> str:
    return f"""
You are an expert prompt evaluator.

Your task is to evaluate the quality of the user's prompt.

USER PROMPT:
{user_prompt}

Evaluate the prompt using these five criteria:

1. Clarity
2. Specificity
3. Context
4. Completeness
5. Expected Output

For each criterion:
- Give a score from 1 to 10.
- Explain the score briefly.

Then provide:

- Overall score from 1 to 10
- Strengths of the prompt
- Problems with the prompt
- Specific suggestions for improvement
- An improved version of the prompt

Be objective and concise.
"""