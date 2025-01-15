from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import run

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Secure Website</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
                text-align: center;
                padding-top: 50px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Secure Website</h1>
        <p>This is a simple FastAPI application served over HTTPS!</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == '__main__':
    # Serve the app with SSL using Uvicorn
    run(app, host="127.0.0.1", port=5000,
        ssl_keyfile="D:/Aarya/Coding_Projects/vulnerable_websites/SSL_certificates/private.key",
        ssl_certfile="D:/Aarya/Coding_Projects/vulnerable_websites/SSL_certificates/certificate.crt")
