# Base image: contains the OS and python version with it
FROM python:3.12-slim

# Environment variables monitoring python:
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Creates /app directory inside a container
# All future commands run from app
WORKDIR /app


# Copies dependencies from requirement text to the working directory
COPY requirements.txt .

# Runs pip install similar to local implementation
RUN pip install --no-cache-dir -r requirements.txt

# Copies everything from project folder into app container
COPY . /app

# Exposes port 8000 ensures container will listen to this post
EXPOSE 8000

# Defines default entrypoint command when container starts
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

