FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first 
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest
COPY . .

# Run uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]