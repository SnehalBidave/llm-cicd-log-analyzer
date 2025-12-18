def extract_errors(log_text: str) -> str:
    """
    Extract only ERROR / FAILED / EXCEPTION lines
    to reduce noise before sending to LLM
    """
    important_lines = []

    for line in log_text.splitlines():
        if any(keyword in line for keyword in ["ERROR", "FAILED", "Exception", "FATAL"]):
            important_lines.append(line)

    if not important_lines:
        return "No explicit error lines found in logs."

    return "\n".join(important_lines[:50])
