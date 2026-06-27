# Start from a minimal official Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (enables layer caching)
COPY requirements.txt .

# Install dependencies from the declaration
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user and switch to it (least privilege)
RUN useradd --create-home appuser
USER appuser

# Document the port the app listens on
EXPOSE 8000

# Command that runs when the container starts
CMD ["python", "main.py"]
