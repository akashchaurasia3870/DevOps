FROM python:3.11-slim

RUN apt-get update && apt-get install -y bash

WORKDIR /app

ADD . .

# ENTRYPOINT ["python"]

CMD ["python","app.py"]
