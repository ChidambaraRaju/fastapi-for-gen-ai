# Rangmanch Review API

A CRUD FastAPI application for storing and managing theatre-play reviews. Unlike the other projects, it persists data in a local SQLite database using SQLModel.

## Run locally

From this directory, install the dependencies and start the development server:

```bash
pip install fastapi "uvicorn[standard]" sqlmodel
uvicorn main:app --reload
```

The app creates `rangmanch.db` during startup. Use `http://127.0.0.1:8000/docs` to explore the API.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Returns a welcome message. |
| `POST` | `/review/` | Creates a review. |
| `GET` | `/review/` | Lists reviews; accepts `play_name`, `skip`, and `limit` query parameters. |
| `GET` | `/review/{review_id}` | Gets a review by ID. |
| `PATCH` | `/review/{review_id}` | Updates a review's rating and/or comment. |
| `DELETE` | `/review/{review_id}` | Deletes a review. |
| `GET` | `/review/average/{play_name}` | Returns the play's average rating and review count. |

Example create request:

```json
{
  "play_name": "Tughlaq",
  "reviewer_name": "Asha",
  "rating": 5,
  "comment": "A compelling production."
}
```

## Key components

- `FastAPI` provides the web application and routes.
- `lifespan` is an `@asynccontextmanager` that creates database tables when the app starts.
- `SQLModel` combines Pydantic validation with SQLAlchemy-style database models.
- `Review` is the database table model; `ReviewCreate`, `ReviewRead`, and `ReviewUpdate` define dedicated API schemas.
- `create_engine` configures SQLite, while `Session` handles individual database transactions.
- `Depends(get_session)` injects a database session into every review route.
- `select` and `func.avg` are used to retrieve reviews and calculate an average rating.

## Development note

The list endpoint accepts `skip` and `limit`, but SQLModel query methods return a new query. To make pagination effective, assign the result back to `query`:

```python
query = query.offset(skip).limit(limit)
```
