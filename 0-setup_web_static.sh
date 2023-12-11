#!/usr/bin/env bash
#script to confugure deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"
sudo mkdir -p /data/
sudo mkdir -p  /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
	<head>
	</head>
	<body>
	 Holberton School
	 </body>
	</html>
" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
nginx_config="/etc/nginx/sites-available/default"
sudo cp "$nginx_config" "$nginx_config.bak"
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
