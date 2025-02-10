# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages (this project only uses Python's standard libraries)
# RUN pip install --no-cache-dir -r requirements.txt

# Run blockchain_simulation.py when the container launches
CMD ["python", "blockchain_simulation.py"]
