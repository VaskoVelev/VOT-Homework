FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask requests minio
CMD ["python", "app.py"]