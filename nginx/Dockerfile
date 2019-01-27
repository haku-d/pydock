# Dockerfile-nginx
FROM nginx:alpine

COPY nginx.conf /etc/nginx/

RUN apk update \
    && apk upgrade \
    && apk add --no-cache openssl \
    && apk add --no-cache bash \
    && adduser -D -H -u 1000 -s /bin/bash www-data

# Remove the default config file that
# /etc/nginx/nginx.conf includes
RUN rm /etc/nginx/conf.d/default.conf

# Nginx will listen on this port
EXPOSE 80 443

ADD ./startup.sh /opt/startup.sh
CMD ["/bin/bash", "/opt/startup.sh"]
