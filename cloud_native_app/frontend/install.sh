sudo mkdir -p /var/www/html
cd frontend
sudo apt-get update
sudo apt-get install -y php apache2 php-curl
sudo cp -r www/ /var/www/html
sudo rm /var/www/html/index.html
./etc/init.d/apache2 start
