FROM node:alpine

WORKDIR /usr/src/requirements

COPY package.json /usr/src/requirements

RUN npm install

WORKDIR /usr/src/finance

CMD ["npm", "start"]