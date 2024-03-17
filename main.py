from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "hello from dev"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
