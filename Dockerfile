# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install system dependencies and MongoDB tools
RUN apt-get update && apt-get install -y \
    postgresql-client \
    redis-tools \
    gnupg \
    curl \
    && curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | gpg --dearmor -o /usr/share/keyrings/mongodb-server-4.4.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg] http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list \
    && apt-get update \
    && apt-get install -y mongodb-org-tools \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Copy the rest of the application code
COPY . .

CMD ["python", "src/main.py"]RUN apt-get update && apt-get install -y \
    postgresql-client \
    redis-tools \
    gnupg \
    curl \
    && curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | gpg --dearmor -o /usr/share/keyrings/mongodb-server-4.4.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg] http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list \
    && apt-get update \
    && apt-get install -y mongodb-org-tools \
    && apt-get install -y rsyslog \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size