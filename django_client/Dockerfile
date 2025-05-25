# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY django_client/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY django_client .

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
