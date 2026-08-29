# Pincode Lookup API

A FastAPI service that looks up Indian location details from a six-digit pincode. The project uses an in-memory pincode data set and demonstrates request validation, response models, batch input, and custom error responses.

## Run locally

From this directory, install the dependencies and start the development server:

```bash
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message. |
| `GET` | `/pincode/{pincode}` | Looks up one valid six-digit pincode. |
| `POST` | `/pincode/bulk` | Looks up multiple pincodes in a JSON request body. |

Example bulk request:

```json
{ "pincodes": ["110001", "560001"] }
```

> **Note:** FastAPI checks routes in declaration order. Move `POST /pincode/bulk` above `GET /pincode/{pincode}` in `main.py` before using the bulk endpoint, otherwise `bulk` is interpreted as the `{pincode}` value.

## Key components

- `FastAPI` hosts the API, while `@app.get` and `@app.post` define routes.
- `pincode_db` in `data.py` is the in-memory lookup data source.
- Pydantic models `LocationResponse`, `BulkRequest`, and `BulkResponse` validate and document API payloads.
- `field_validator` checks that pincodes contain exactly six digits and that bulk requests contain 1–20 values.
- `PinCodeNotFoundError` and `InvalidPinCodeError` are custom exceptions.
- Custom exception handlers return consistent JSON errors with appropriate `404` and `400` status codes.
