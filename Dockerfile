FROM python:3.10.12
WORKDIR /app 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "debit_api:app", "--host", "0.0.0.0", "--port", "8000"]

#how to run 
# sudo docker run  -p 8000:8000 <image_name>
