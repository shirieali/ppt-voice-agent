from fastapi import FastAPI
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

        <form action="/upload" method="post"e" name="file" accept=".pptx">
            <button type="submit">Upload PPT</button>
        </form>
    </body>
    </html>
    """
