FROM python:3.12-slim

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.description="ML inference API for student MLOps exercise" \
      org.opencontainers.image.vendor="student"

ARG APP_VERSION=1.0.0
ARG VCS_REF=unknown

LABEL org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
