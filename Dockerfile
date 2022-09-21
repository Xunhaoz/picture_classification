FROM ubuntu:20.04

WORKDIR /app

ADD . /app

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

CMD python3 classification.py
