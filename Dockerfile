FROM orchardup/python:2.7
ADD . /code
WORKDIR /code
CMD python check_status.py
