FROM python:3.10

COPY days.py /app/days.py

WORKDIR /app

CMD ["python", "days.py"]
