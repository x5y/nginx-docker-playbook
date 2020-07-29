FROM nginx
COPY static-html /usr/share/nginx/html

HEALTHCHECK CMD curl -s -o /dev/null -w "%{http_code}" localhost | grep 200