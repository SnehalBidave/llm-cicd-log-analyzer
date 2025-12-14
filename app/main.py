from fastapi import FastAPI, UploadFile, File
from app.llm import analyze_log

app = FastAPI(title="LLM CI/CD Log Analyzer")

@app.post("/analyze")
async def analyze_log_file(file: UploadFile = File(...)):
    log_text = (await file.read()).decode("utf-8")
    result = analyze_log(log_text)
    return {"analysis": result}
