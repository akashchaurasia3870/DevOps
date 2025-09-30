FROM node:16-alpine

WORKDIR /app

RUN touch a.txt 

RUN echo hi

ADD . .

ENTRYPOINT ["node"]

CMD ["app.js"]