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
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }

            h1 {
                color: #1f4e79;
            }

            button {
                padding: 10px 20px;
                cursor: pointer;
            }
        </style>
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
        "status": "Upload successful",
        "saved_to": file_path
    }
