FROM python:3.6.3

ENV SLACK_TOKEN             xoxp-1419412195043-1412474060998-1480036020055-042d6981cea6ebf4b9556f2e6d33cf2f
ENV SLACK_SIGNING_SECRET    2f0093fa35d3d48a15eb6626ba0eb00d

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]