FROM node:alpine

WORKDIR /usr/src/finance

COPY package.json /usr/src/finance

RUN npm install

COPY . /usr/src/finance

CMD ["npm", "start"]