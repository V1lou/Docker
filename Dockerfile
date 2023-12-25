FROM python:3.10.13-bookworm

COPY days.py /app/days.py

WORKDIR /app

CMD ["python", "days.py"]
