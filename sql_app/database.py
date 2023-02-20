from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme="postgresql",
    user="docker",
    password="docker",
    host="postgres",
    path=f"/{'docker' or ''}",
)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://docker:docker@192.168.112.3/docker"
# SQLALCHEMY_DATABASE_URL = "postgresql://docker:docker@localhost/docker"

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URI, pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# uvicorn sql_app.main:app --reload