# postgresql with api endpoints

```bash
docker-compose up
```

The postgresql is at network name postgres:5432
```python
SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme="postgresql",
    user="docker",
    password="docker",
    host="postgres",
    path=f"/{'docker' or ''}",
)
```

pgadmin is at localhost:1235

The api endpoints are at localhost:8001
