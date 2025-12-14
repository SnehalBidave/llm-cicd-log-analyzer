import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_log(log_text: str) -> str:
    prompt = f"""
You are a senior DevOps engineer.
Analyze the following CI/CD or application log.
Explain the root cause in simple words.
Suggest step-by-step fixes.

LOG:
{log_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
