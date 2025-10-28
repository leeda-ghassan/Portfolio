# Use an official Python runtime as a parent image
FROM python:3.12-slim-buster

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
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]