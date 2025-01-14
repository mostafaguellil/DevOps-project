FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 7000

# Run the application
CMD ["python", "app.py"]