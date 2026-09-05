# Dabbewala API

A FastAPI application for managing tiffin (dabba) delivery orders. It persists orders in a local SQLite database with SQLModel, splits routes across routers, and exposes a daily status summary.

## Run locally

From this directory, install the dependencies and start the development server:

```bash
pip install fastapi "uvicorn[standard]" sqlmodel
uvicorn main:app --reload
```

The app creates `dabbewala.db` during startup. Use `http://127.0.0.1:8000/docs` to explore the API.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/orders/` | Creates an order. Status defaults to `preparing`. |
| `GET` | `/orders/` | Lists orders; accepts `status`, `created_date`, `skip`, and `limit` query parameters. |
| `GET` | `/stats/orders` | Returns a count of orders by status for a given date (defaults to today). |

Example create request:

```json
{
  "customer_name": "Meera",
  "delivery_address": "12 Marine Drive, Mumbai",
  "items": "dal, roti, sabzi"
}
```

Order status values: `preparing`, `picked_up`, `in_transit`, `delivered`.

Example daily summary response:

```json
{
  "date": "2026-09-05",
  "summary": {
    "preparing": 2,
    "picked_up": 1,
    "in_transit": 0,
    "delivered": 3
  },
  "total": 6
}
```

## Key components

- `FastAPI` hosts the API; `APIRouter` groups order and stats routes in `routes/`.
- `lifespan` is an `@asynccontextmanager` that creates database tables when the app starts.
- `SQLModel` combines Pydantic validation with SQLAlchemy-style database models.
- `Order` is the database table model; `OrderCreate` and `OrderUpdate` define dedicated API schemas.
- `OrderStatus` is a string `Enum` for the delivery lifecycle.
- `create_engine` configures SQLite, while `Session` handles individual database transactions.
- `Depends(get_session)` injects a database session into order and stats routes.
- `select` and `func.count` are used to list orders and build the daily status summary.

## Development note

The list endpoint documents `created_date` as `YYYY-MM-DD`, but the parameter is typed as `str`. Parse it to a `date` before combining with times, otherwise `datetime.combine` will raise a `TypeError`:

```python
from datetime import date

created_on = date.fromisoformat(created_date)
start = datetime.combine(created_on, datetime.min.time())
end = datetime.combine(created_on, datetime.max.time())
```
