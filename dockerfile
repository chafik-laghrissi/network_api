FROM python:3.8-alpine
RUN apt-get update && apt-get install --yes libgdal-dev
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]  