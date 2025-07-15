FROM python:3.11-slim
WORKDIR /code
COPY tasks/fastapi_sync_async/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn[standard]==0.29.0
COPY tasks/fastapi_sync_async /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

