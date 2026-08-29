# SQLModel defines our database-table models and keeps track of their metadata.
# Session is the object we use to read, add, update, and delete database records.
# create_engine creates the shared connection configuration for our database.
from sqlmodel import SQLModel, Session, create_engine

# SQLite stores the whole database in a local file. This URL creates/uses
# rangmanch.db in this project's current directory.
DATABASE_URL = "sqlite:///rangmanch.db"

# The engine does not open a database connection immediately; it stores the
# details SQLModel needs whenever it later needs to communicate with SQLite.
# echo=True logs every generated SQL statement to the console, which helps us
# learn, inspect, and debug the database queries SQLModel generates.
engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    """Create any tables declared by our SQLModel models that do not exist yet."""
    # SQLModel.metadata contains every table model imported before this function
    # runs. create_all checks each one and creates its SQLite table if needed;
    # it does not delete existing tables or their data.
    SQLModel.metadata.create_all(engine)


def get_session():
    """Provide one database session to a request, then close it afterwards."""
    # A session is a short-lived workspace for database operations in one request.
    # FastAPI receives the yielded session and injects it into route functions.
    with Session(engine) as session:
        yield session
    # When the request is done, leaving the `with` block closes the session,
    # returning its database resources safely.
