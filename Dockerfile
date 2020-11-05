FROM python:3.7

ADD . /src

RUN pip install numpy scipy

CMD ["python", "-m", "unittest", "discover", "-s","/src/tests"]