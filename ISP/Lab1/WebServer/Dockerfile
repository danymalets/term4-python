FROM python:3.8

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

EXPOSE 8000

COPY . /usr/src/app/

RUN pip install -r requirements.txt

CMD ["python", "main.py"]