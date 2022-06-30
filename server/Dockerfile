FROM ubuntu:18.04
COPY . /server
RUN apt-get update
RUN apt-get install python3-pip -y
RUN ln -s $(which python3) /bin/python
RUN python -m pip install -U --force-reinstall pip
RUN pip3 install -r server/requirements.txt
WORKDIR /server
ENTRYPOINT ["./entrypoint.sh"]