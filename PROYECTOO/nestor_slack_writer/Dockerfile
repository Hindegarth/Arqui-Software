FROM python:3.6.3

ENV SLACK_TOKEN     xoxp-1419412195043-1412474060998-1480036020055-042d6981cea6ebf4b9556f2e6d33cf2f

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]