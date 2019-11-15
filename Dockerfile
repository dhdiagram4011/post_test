FROM centos:latest
MAINTAINER dhdiagram<dhdiagram@gmail.com>
add ./matser.zip /opt
RUN yum install -y zip unzip
RUN cd /opt && unzip .
RUN yum install -y python3*
RUN yum install python3-pip
RUN pip3 install requests
RUN pip3 install django
RUN cd /learning-english-by-youtube-subtitle--master/testcode/tcode
CMD nohup python3 manage.py runserver 0:8000 &

