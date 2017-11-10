FROM python:3.6

RUN mkdir /src
WORKDIR /src

COPY requirements.txt requirements.txt
COPY scripts/start.sh start.sh
COPY gqlclans gqlclans
COPY start_app.py start_app.py
COPY tests tests
COPY tox.ini tox.ini
RUN pip install tox
RUN pip install -r requirements.txt
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

EXPOSE 8567

CMD /src/start.sh
