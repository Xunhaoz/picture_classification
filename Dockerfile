FROM python:3.6.9

WORKDIR /app

ADD . /app

RUN pip install Flask
RUN pip install matplotlib
RUN pip install wheel
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

CMD python classification.py