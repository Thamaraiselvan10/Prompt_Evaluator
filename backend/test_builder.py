from prompt_builder import build_evaluation_prompt

prompt="i have 2 apple there are three member, how do i cut it?"

evaluation_prompt=build_evaluation_prompt(prompt)

print(evaluation_prompt)