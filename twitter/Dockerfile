FROM node:14

WORKDIR /usr/src/app/twitter

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]