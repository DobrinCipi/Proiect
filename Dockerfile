FROM python:3.11
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /application
WORKDIR /application
COPY Catalog_Digital .
ENTRYPOINT [ "python", "manage.py", "runserver", "0:8000" ]