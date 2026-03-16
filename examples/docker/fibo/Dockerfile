# A lightweight Python image as parent
FROM python:3.7-alpine

# Set working directory to /dirInContainer
WORKDIR /dirInContainer

# Copy python script fibo.py to the working directory
COPY fibo.py .

# Execute python script
CMD ["python", "fibo.py"]
