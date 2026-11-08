from fastapi import FastAPI

app = FastAPI(title="VaultDrop")

@app.get("/health")

def health():
	return {"status": "ok"}
