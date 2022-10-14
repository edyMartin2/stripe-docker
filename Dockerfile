FROM python:3.6
COPY . /app
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
