FROM python:2.7
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "mysite.settings"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
ADD ./static/ /usr/local/src/app/static/
ADD . /code/
