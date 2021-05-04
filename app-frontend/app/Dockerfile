FROM node:12 as node

ADD . /var/www/app
WORKDIR /var/www/app
RUN yarn install
RUN yarn build



FROM caddy
COPY Caddyfile /etc/Caddyfile
COPY --from=node /var/www/app/dist /srv

# WORKDIR /var/www/app/dist
# RUN curl --output caddy "https://caddyserver.com/api/download?os=linux&arch=amd64&idempotency=85375124104505" && chmod a+x caddy
# CMD ["./caddy", "run"]