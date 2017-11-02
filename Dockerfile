FROM python:3.6

RUN mkdir /src
WORKDIR /src

COPY requirements.txt requirements.txt
COPY scripts/start.sh .src/start.sh
COPY gqlclans gqlclans
COPY tests tests
COPY tox.ini tox.ini
RUN pip install tox
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD start.sh
