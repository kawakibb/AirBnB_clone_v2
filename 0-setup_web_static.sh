#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

# Install Nginx if not already installed
if ! dpkg -l | grep -q "nginx"; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
if [ ! -d "/data" ]; then
    mkdir /data
fi

if [ ! -d "/data/web_static" ]; then
    mkdir /data/web_static
fi

if [ ! -d "/data/web_static/releases" ]; then
    mkdir /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ]; then
    mkdir /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test" ]; then
    mkdir /data/web_static/releases/test
fi

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L "/data/web_static/current" ]; then
    rm -f /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sed -i "24i\    location /hbnb_static {\n        alias /data/web_static/current/;\n    }" $config_file

# Restart Nginx
service nginx restart
