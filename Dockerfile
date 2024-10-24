FROM python:3.9

# Set the working directory in the container
WORKDIR /Cloud/venv


COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "exo2:app", "--host", "0.0.0.0", "--port", "8000"]


