# Use the official Python base image (slim version recommended for smaller size)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies first to optimize build cache
# This ensures the dependency layer is only rebuilt if requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY api_corrected.py .

# Port 5000 is the port Flask is listening on (and will be mapped by docker-compose)
EXPOSE 5000

# Command to execute the application when the container starts
# We use Python to start the script
CMD ["python", "api_corrected.py"]