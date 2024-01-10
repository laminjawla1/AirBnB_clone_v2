#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

# Update and upgrade packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install nginx if not exists
sudo apt-get install nginx

# Create the required folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
sudo echo "<h1>Some Dummy Heading</h1>" | tee /data/web_static/releases/test/index.html

# Delete the symbolic link if it exists else handle the exception
# and create the actual symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Ownership and group to ubuntu recursive
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx confuguration to server the content of
# /data/web_static/ to hbnb_static
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# Restart the nginx service
sudo service nginx restart
