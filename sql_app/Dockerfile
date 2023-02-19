
# https://fastapi.tiangolo.com/deployment/docker/#:~:text=Go%20to%20the%20project%20directory%20%28in%20where%20your,your%20current%20server%20%28and%20number%20of%20CPU%20cores%29.
FROM python:3.11
WORKDIR /workspace
COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /workspace/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]