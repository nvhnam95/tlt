# Build stage
FROM node:13.12.0 as BUILD
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY view/package.json ./
COPY view/package-lock.json ./
RUN npm install --silent
COPY view/ ./
RUN npm run build
 
# Deploy stage
FROM nginx:stable-alpine
COPY --from=BUILD ./app/dist/ /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

