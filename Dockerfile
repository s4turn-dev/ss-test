from python:latest

copy ./requirements.txt req.txt
RUN pip install --no-cache-dir --upgrade -r req.txt
EXPOSE 5000
COPY . .

RUN chmod +x wait-for-it.sh
RUN chmod +x docker-entrypoint.sh
