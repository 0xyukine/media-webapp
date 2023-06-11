FROM node:18

WORKDIR /web-img-browser

COPY package*.json ./
COPY . .

RUN npm install express

CMD ["node", "index.js"]