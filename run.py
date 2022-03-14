from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)


if __name__ == "__main__":
    uvicorn.run("run:app", host='0.0.0.0', port=6111, reload=True)
