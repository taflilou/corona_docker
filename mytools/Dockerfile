FROM centos:latest

MAINTAINER Abdel TESSILIMI

RUN yum -y update 
RUN yum -y install git python3-pip python2-pip jq mlocate nc net-tools vim
RUN updatedb
RUN ln -s /usr/bin/pip3.6 /usr/bin/pip
RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN pip install --upgrade pip
RUN pip install wheel pipenv
RUN mkdir -p /vagrant/statscorona

ADD /statscorona /vagrant/statscorona
WORKDIR /vagrant/statscorona

RUN pip install flask
RUN pip install -r /vagrant/statscorona/requirements.txt

ENV FLASK_APP /vagrant/statscorona/corona.py
ENV FLASK_ENV development

EXPOSE 5000

CMD [ "python corona.py" ]
ENTRYPOINT python corona.py

# CMD [ "python corona.py" ]
# CMD ["flask run --host=0.0.0.0"]
