from fastapi.responses import JSONResponse
from fastapi import Request


class PinCodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode

class InvalidPinCodeError(Exception):
    def __init__(self, pincode: str, reason:  str = "Invalid format"):
        self.pincode = pincode
        self.reason = reason

# Custom handlers

async def pincode_not_found_handler(request: Request, exception: PinCodeNotFoundError):
    return JSONResponse(
        status_code= 404,
        content= {
            "error": "pincode_not_found",
            "message": f"No location for pincode {exception.pincode}",
            "pincode": exception.pincode
        }
    )

async def invalid_pincode_handler(request: Request, exception: InvalidPinCodeError):
    return JSONResponse(
        status_code= 400,
        content= {
            "error": "invalid_pincode",
            "message": f"Pincode {exception.pincode} is invalid: {exception.reason}",
            "pincode": exception.pincode
        }
    )