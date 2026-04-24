FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install -e .

CMD ["python", "-m", "src.main"]
