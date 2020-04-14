FROM python:3.6-alpine
RUN pip install pipenv
COPY . /vulnapp
WORKDIR /vulnapp
RUN pipenv install --deploy --ignore-pipfile
CMD ["pipenv", "run", "python", "main.py"]