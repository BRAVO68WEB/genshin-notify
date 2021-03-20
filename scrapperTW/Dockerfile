FROM node:14

WORKDIR /usr/src/app/scrapperTW

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]