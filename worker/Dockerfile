FROM python:3.12-slim

WORKDIR /worker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# comandi cmd per avviare il worker 
CMD ["python", "-u", "worker.py"]
