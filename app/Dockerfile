# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update && apt-get install -y libpq-dev


# Copy the main.py file into the container at /app
COPY app.py /app
COPY person.sql /app

# Run the command to start the application
CMD ["python", "app.py"]