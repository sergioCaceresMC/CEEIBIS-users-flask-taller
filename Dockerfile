FROM python:3.12-slim

# Dependencias nativas para mysqlclient
RUN apt update && apt install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "--app", "index", "run", "--host=0.0.0.0", "--port=5000"]
