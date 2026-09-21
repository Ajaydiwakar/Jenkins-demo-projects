# Stage 1: Build dependencies
FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Final runtime image
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_tracker.wsgi:application"]
