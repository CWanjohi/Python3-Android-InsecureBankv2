FROM python:3.9

RUN useradd -m adrserver
WORKDIR /app
COPY src/ .
RUN apt update -y
RUN pip install --upgrade --no-cache-dir Flask==2.0.2 SQLAlchemy==1.4.22 waitress==2.0.0
RUN chown -R root:adrserver /app && \
    chmod 750 /app /app/app.py
USER adrserver
CMD ["/usr/local/bin/python", "/app/app.py"]
EXPOSE 8888
