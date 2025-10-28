# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your Flask app runs on (default is 5000)
EXPOSE 5000

# Define the command to run your Flask application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "4"]