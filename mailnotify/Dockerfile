FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python python-pip cron -y
RUN pip install pymongo
ADD mailNotify.py /
ADD crontab /etc/cron.d/
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
