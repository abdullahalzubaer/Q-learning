FROM python:3.7-slim

LABEL DEVELOPER="Abdullah Al Zubaer"

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

# ENTRYPOINT ["python", "q_learning.py"]
