# 0x1A-application_server

This directory contains the setup and configuration for serving various projects developed within the AirBnB clone series using Gunicorn and Nginx.

## 0. Set up development with Python

### Requirements:

- Task #3 of your SSH project completed for web-01.
- `net-tools` package installed on your server: `sudo apt install -y net-tools`.
- AirBnB_clone_v2 cloned on your web-01 server.
- Configured `web_flask/0-hello_route.py` to serve content from the route `/airbnb-onepage/` on port 5000.
- Flask application object named `app`.

## 1. Set up production with Gunicorn

### Requirements:

- Gunicorn and any required libraries installed.
- Flask application object named `app`.
- Serving content from the same route as in the previous task.
- Gunicorn instance bound to localhost on port 5000 with the application object as the entry point.
- Checker will bind a Gunicorn instance to port 6000 for verification.

## 2. Serve a page with Nginx

### Requirements:

- Nginx serving the page locally and on its public IP on port 80.
- Nginx proxying requests to the process listening on port 5000.
- Include Nginx config file as `2-app_server-nginx_config`.

### Notes:

- Spin up either your production or development application server (listening on port 5000) to test.
- In a production environment, the application server will be configured to start upon startup.

## 3. Add a route with query parameters

### Requirements:

- Nginx serving the page locally and on its public IP on port 80.
- Nginx proxying requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance on port 5001.
- Include Nginx config file as `3-app_server-nginx_config`.

### Tips:

- Configure Nginx to proxy requests to processes listening on two different ports.

## 4. Let's do this for your API

### Requirements:

- AirBnB_clone_v3 cloned.
- Nginx configured to route `/api/` to a Gunicorn instance on port 5002.
- Nginx serving the page locally and on its public IP on port 80.
- Gunicorn bound to `api/v1/app.py` for testing.
- Nginx config file uploaded as `4-app_server-nginx_config`.

## 5. Serve your AirBnB clone

### Requirements:

- AirBnB_clone_v4 cloned.
- Gunicorn serving content from `web_dynamic/2-hbnb.py` on port 5003.
- Nginx routes `/` to the Gunicorn instance.
- Nginx serves static assets found in `web_dynamic/static/`.
- Website must be fully functional, reconfigure `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.
- Nginx serving the page locally and on its public IP on port 5003.
- Nginx config uploaded as `5-app_server-nginx_config`.
