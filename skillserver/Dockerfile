FROM python:3.6
MAINTAINER Florian Zimmermeister "zimmermeister@a-ware.io"
copy . /app
WORKDIR /app
RUN pip3 install Cython
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
