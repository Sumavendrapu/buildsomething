# Use a Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port
EXPOSE 5000

# Command to run the app
CMD ["python", "book_service.py"]
