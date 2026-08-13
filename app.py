from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

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
            <input type="file" name="file" accept=".pptx">
            <button type="submit">Upload PPT</button>
        </form>
    </body>
    </html>
    """

@app.post("/upload")
async def upload_ppt(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "status": "Upload successful"
    }
