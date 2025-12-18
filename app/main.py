from fastapi import FastAPI, UploadFile, File
from app.log_parser import extract_errors
from app.llm import analyze_log

app = FastAPI(title="LLM CI/CD Log Analyzer")

@app.get("/")
def health_check():
    return {"status": "LLM CI/CD Log Analyzer is running"}

@app.post("/analyze")
async def analyze_log_file(file: UploadFile = File(...)):
    raw_log = (await file.read()).decode("utf-8")

    # Step 1: Extract important error lines
    cleaned_log = extract_errors(raw_log)

    # Step 2: Analyze using LLM
    analysis = analyze_log(cleaned_log)

    return {
        "filename": file.filename,
        "analysis": analysis
    }
