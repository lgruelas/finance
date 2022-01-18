FROM node:16

WORKDIR /usr/src/finance

COPY package*.json /usr/src/finance/

RUN npm install

ENV PATH /usr/src/finance/node_modules/.bin:$PATH

WORKDIR /usr/src/finance/app

CMD ["npm", "start"]