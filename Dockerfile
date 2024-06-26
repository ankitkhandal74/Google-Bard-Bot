FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y && apt install git -y

COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

RUN mkdir /Google-Bard-Bot
WORKDIR /Google-Bard-Bot
COPY bot.py /Google-Bard-Bot/

CMD ["python", "bot.py"]
