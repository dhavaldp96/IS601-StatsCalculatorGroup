FROM python:3.7

ADD . /src

RUN pip install -r /src/requirements.txt

CMD ["python", "-m", "unittest", "discover", "-s","/src/tests"]