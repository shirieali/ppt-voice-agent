from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PPT Voice Agent</title>
    </head>
    <body>
        <h1>PPT Voice Agent</h1>
        <p>Upload a PowerPoint presentation and generate narration.</p>

        /upload
            <input type="file" name="file" accept=".ppt,.pptx" required>
            <br><br>
            <button type="submit">Upload PPT</button>
        </form>

    </body>
    </html>
    """

@app.post("/upload")
async def upload_ppt(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        contents = await file.read()
        buffer.write(contents)

    return {
        "filename": file.filename,
        "status": "Upload successful"
    }
