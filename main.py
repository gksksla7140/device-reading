from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api import router as api_router
from app.exceptions import DeviceNotFound

app = FastAPI()

app.include_router(api_router)

@app.exception_handler(DeviceNotFound)
async def device_not_found_exception_handler(request, exc: DeviceNotFound):
    error_message = f"Device with ID {exc.device_id} not found"
    error_response = {"error": error_message}
    return JSONResponse(content=error_response, status_code=404)