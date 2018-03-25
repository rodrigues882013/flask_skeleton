FROM python:3-alpine

RUN mkdir -p /usr/src/application
WORKDIR /usr/src/application

COPY . /usr/src/application
RUN pip install -r requirements.txt

ENTRYPOINT [ "gunicorn" ]

CMD ["--bind", "0.0.0.0", "wsgi:app" ]

# Expose the Flask port
EXPOSE 8000