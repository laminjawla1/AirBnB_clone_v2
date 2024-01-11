#!/usr/bin/env bash
# A script to setup a web server for deployment.

# Update and upgrade the packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install nginx
sudo apt-get install nginx -y

# Creating the necessary directoris
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Dummy content for testing
echo "<!DOCTYPE html>
<html lang='en'>
  <head>
  	<title>Testing The Nginx Web Server</title>
  </head>
  <body>
  	<h1>Some Dummy Heading</h1>
  </body>
</html>" | tee /data/web_static/releases/test/index.html

# Create a 'current' symlink and if exist, delete and recreate
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Make the owner and group to be ubuntu
chown -R ubuntu:ubuntu /data

sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
sudo service nginx restart
