FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["/bin/sh", "-c", "python app/init_test_data.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
