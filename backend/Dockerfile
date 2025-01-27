
FROM python:3.10-alpine


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]