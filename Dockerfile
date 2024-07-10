FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip3 install -r req.txt
CMD ["python3", "main.py"]