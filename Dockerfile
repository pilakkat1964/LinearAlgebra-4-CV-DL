FROM python:3.12-slim

WORKDIR /workspace

# Install system deps often required for scientific packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy minimal project files for installing dependencies
COPY requirements-base.txt requirements-base-locked.txt requirements-heavy-locked.txt requirements-manim-locked.txt ./

# Create venv and install base requirements
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements-base-locked.txt

# (Optional) Install heavy requirements if the image is built with BUILD_HEAVY=1
ARG BUILD_HEAVY=0
RUN if [ "$BUILD_HEAVY" = "1" ]; then pip install -r requirements-heavy-locked.txt; fi

# (Optional) Install Manim and the system deps it commonly requires when BUILD_MANIM=1
ARG BUILD_MANIM=0
RUN if [ "$BUILD_MANIM" = "1" ]; then \
      apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        pkg-config \
        fonts-dejavu-core \
        texlive-latex-recommended \
        texlive-latex-extra \
        dvipng \
      && rm -rf /var/lib/apt/lists/* \
      && pip install -r requirements-manim-locked.txt; \
    fi

# Copy source
COPY . /workspace

CMD ["/bin/bash"]
