# Chai Menu API

A small, read-only FastAPI service that exposes a fictional Chai Point-style menu. It demonstrates how to return validated JSON responses and filter an in-memory collection with query parameters.

## Run locally

From this directory, install the dependencies and start the development server:

```bash
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the API in FastAPI's interactive Swagger UI.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message. |
| `GET` | `/menu` | Returns every menu item. Use `?category=Chai` to filter by category. |
| `GET` | `/menu/{item_id}` | Returns one menu item by its numeric ID. |

An unknown category or item ID returns a `404 Not Found` response.

## Key components

- `FastAPI` creates the application and defines the HTTP routes.
- `Query` describes the optional `category` query parameter.
- `Path` validates and documents the `item_id` path parameter.
- `HTTPException` produces clear `404` API errors.
- `MenuItem` and `MenuResponse` are Pydantic `BaseModel` classes that validate and document the response structure.
- `chai_menu` in `data.py` is the in-memory data source used by the API.
