FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y python3.11 python3.11-venv && \
    python3.11 -m venv /opt/venv && \
    apt-get clean

COPY . .

RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
