FROM python:3.6
MAINTAINER hulk.oh "snuboy89@gmail.com"

ENV TZ ROK

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ./app /app/
WORKDIR /app

EXPOSE 80
CMD ["python", "github_make_song.py"]