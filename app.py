from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body>
        <h1>PPT Voice Agent</h1>

        <formad
            <input type="file" name="file" accept=".pptx">
            <button type="submit">Upload PPT</button>
        </form>

    </body>
    </html>
    """

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "status": "Upload successful"
    }
