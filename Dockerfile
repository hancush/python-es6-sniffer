FROM python:3.8
MAINTAINER "DataMade <info@datamade.us>"

RUN pip install git+https://github.com/hancush/python-es6-sniffer

CMD ["es6-sniffer"]
