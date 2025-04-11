FROM python:latest
COPY hello.py .
CMD ["python", "main.py"]
