# Microservices with python
## created api's using fast api
You can may use a virtual environment or not.
how to run: 
pip install fastapi
pip install uvicorn
pip install "uvicorn[standard]"

# or via Docker(make sure you have docker in your machine) 
how to build and run: 
docker build -t image_name .
docker run  -p 8000:8000 <image_name>
Swagger UI url wil be: 
http://0.0.0.0:8000/docs
