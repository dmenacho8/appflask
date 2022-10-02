FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["python3", "app.py"]
