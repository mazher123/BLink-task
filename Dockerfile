FROM python:3.8

# Make a directory for our application
WORKDIR /application
# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy our source code
COPY /app .

# Run the application
CMD ["python", "main.py"]