FROM python:3.7-slim
RUN pip install flask
COPY connection.py /connection.py
CMD ["python", "connection.py"]
