# Use the official Python 3.10 image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependicied for dlib (CMake, build tools, and libraries)
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \ 
    libx11-dev \
    libgtk2.0-dev \ 
    libboost-all-dev \
    && apt-get clean

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/main.py"]
