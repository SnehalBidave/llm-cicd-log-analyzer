def extract_errors(log_text: str) -> str:
    lines = log_text.splitlines()
    error_lines = [
        line for line in lines
        if "ERROR" in line or "FAILED" in line or "Exception" in line
    ]
    return "\n".join(error_lines[:50])
