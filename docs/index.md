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
