import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_log(log_text: str) -> str:
    prompt = f"""
You are a senior DevOps engineer.

Analyze the following CI/CD or application logs.

Your task:
1. Identify the root cause
2. Explain the issue in simple words
3. Provide step-by-step fix
4. Suggest prevention best practices

LOG DATA:
{log_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
