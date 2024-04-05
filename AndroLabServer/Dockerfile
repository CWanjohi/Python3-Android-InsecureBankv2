FROM python:3.9.17-slim-bullseye

RUN useradd -m adrserver
WORKDIR /app
COPY src/ .
COPY requirements.txt requirements.txt
RUN apt update -y
RUN pip install --upgrade --no-cache-dir -r requirements.txt
RUN chown -R root:adrserver /app && chmod 750 /app /app/app.py
USER adrserver
CMD ["/usr/local/bin/python3", "/app/app.py", "--log"]
# CMD ["/usr/local/bin/python3", "/app/app.py"] Uncomment if you do not want to show logs on Docker container logs
EXPOSE 8888
