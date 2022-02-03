FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip3 install --upgrade pip 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]  