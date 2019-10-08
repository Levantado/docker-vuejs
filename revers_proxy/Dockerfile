FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY /prod.conf /etc/nginx/conf.d
COPY /nginx.conf /etc/nginx/
