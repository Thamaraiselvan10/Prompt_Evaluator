import sys
from pathlib import Path

import streamlit as st # streamlit library


project_root = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(project_root))


from backend.evaluator import evaluate_prompt


st.title("Prompt Evaluator")

st.write("Evaluate and improve your AI prompts.")


prompt = st.text_area(
    "Enter your prompt",
    placeholder="Type your prompt here..."
)


if st.button("Evaluate Prompt"):

    if prompt.strip():

        result = evaluate_prompt(prompt)

        st.write(result)

    else:

        st.warning("Please enter a prompt first.")