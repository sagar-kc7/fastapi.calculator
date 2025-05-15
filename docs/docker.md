## How to Run Using Docker

To run this FastAPI calculator app using Docker, follow these steps:

1. Prerequisites
   Install Docker on your machine.

2. Build the Docker Image

   docker build -t fastapi-calculator .

3. Run the Docker Container

   docker run -d -p 8000:8000 fastapi-calculator

4. Access the API
   Once the container is running, open your browser and go to:

http://localhost:8000

You can view the interactive Swagger docs at:

http://localhost:8000/docs

And the ReDoc documentation at:

http://localhost:8000/redoc
