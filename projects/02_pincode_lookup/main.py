from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from data import pincode_db
'''
# This stands in for a database or an external pincode service for now.
PINCODE_LOCATIONS = {
    "110001": {
        "city": "New Delhi",
        "state": "Delhi",
        "district": "New Delhi",
    },
    "400001": {
        "city": "Mumbai",
        "state": "Maharashtra",
        "district": "Mumbai",
    },
    "560001": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "district": "Bengaluru Urban",
    },
}
'''
from exceptions import PinCodeNotFoundError, InvalidPinCodeError, pincode_not_found_handler, invalid_pincode_handler
from models import LocationResponse, BulkResponse, PincodeRequest, BulkRequest

app = FastAPI(
    title= "Pincode Lookup API",
    description= "Autofill city and state from Indian pincode during checkout"
)

#register custom exception handlers
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)

@app.get("/")
def root():
    return {"message": "Pincode Lookup API"}

'''
def validate_pincode(pincode: str) -> str:
    """Validate the path value with the Pydantic request model."""
    try:
        return PincodeRequest(pincode=pincode).pincode
    except ValidationError as error:
        errors = error.errors()
        for item in errors:
            item["loc"] = ("path", "pincode")
        raise RequestValidationError(errors)
'''
'''
@app.get("/pincode/{pincode}", response_model=LocationResponse)
def lookup_pincode(pincode: str = Depends(validate_pincode)):
    """Return location details for a valid six-digit Indian pincode."""
    location = PINCODE_LOCATIONS.get(pincode)

    if location is None:
        raise PinCodeNotFoundError(pincode)

    return LocationResponse(pincode=pincode, **location)
    # We could've used something like the commented lines to use the pydantic validation, but to our custom exception we are implementing in that way
'''

@app.get("/pincode/{pincode}", response_model=LocationResponse)
def lookup_pincode(pincode: str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise InvalidPinCodeError(pincode= pincode, reason= "Pincode must be exactly 6 digits")
    if pincode not in pincode_db:
        raise PinCodeNotFoundError(pincode= pincode)
    return pincode_db[pincode]
    
@app.post("/pincode/bulk", response_model= BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []

    for pincode in request.pincodes:
        if pincode in pincode_db:
            results.append(pincode_db[pincode])
        else:
            missing.append(pincode)

    return BulkResponse(
        found= len(results),
        not_found= len(missing),
        result= results,
        missing = missing
    )