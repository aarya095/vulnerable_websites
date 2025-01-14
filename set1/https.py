from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, HTTPS world!"}

if __name__ == '__main__':
    # Serve the app with SSL using Uvicorn
    run(app, host="127.0.0.1", port=5000,
        ssl_keyfile="D:/Aarya/Coding_Projects/vulnerable_websites/SSL_certificates/private.key",
        ssl_certfile="D:/Aarya/Coding_Projects/vulnerable_websites/SSL_certificates/certificate.crt")
