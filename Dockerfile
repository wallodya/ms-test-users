FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 8888
CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8888"]