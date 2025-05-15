# 🧮 FastAPI Calculator

A simple calculator API built with **FastAPI** that supports basic arithmetic operations: addition, subtraction, multiplication, and division.
This project follows the **12-Factor App** principles and is containerized using **Docker**.

---

## Features

- Addition: `/add?a=2&b=3`
- Subtraction: `/subtract?a=5&b=2`
- Multiplication: `/multiply?a=4&b=3`
- Division (with zero-check): `/divide?a=10&b=2`
- Environment-based configuration using `.env`
- Auto-generated interactive docs at `/docs`

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic Settings
- Docker + Docker Compose
- Uvicorn ASGI server

---

## Configuration

Create a `.env` file at the project root with the following content (example):

```env
APP_NAME=Calculator
DEBUG=False
VERSION=1.0
```

## How to Run Using Docker

To run this FastAPI calculator app using Docker, follow these steps:

1. Prerequisites
   Install Docker on your machine.

2. Build the Docker Image
   bash
   Copy
   Edit
   docker build -t fastapi-calculator .
3. Run the Docker Container
   bash
   Copy
   Edit
   docker run -d -p 8000:8000 fastapi-calculator
4. Access the API
   Once the container is running, open your browser and go to:

arduino
Copy
Edit
http://localhost:8000
You can view the interactive Swagger docs at:

bash
Copy
Edit
http://localhost:8000/docs
And the ReDoc documentation at:

bash
Copy
Edit
http://localhost:8000/redoc
