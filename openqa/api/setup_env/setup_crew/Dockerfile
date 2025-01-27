FROM debian:bookworm

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    git \
    && apt-get clean

# Install pyenv
RUN curl https://pyenv.run | bash

RUN pyenv install 3.11 \
    && pyenv global 3.11

RUN pyenv rehash

RUN python -m venv /opt/os_venv

COPY . .

RUN /opt/os_venv/bin/pip install --no-cache-dir -r requirements.txt
