cd frontend
sudo apt-get update
sudo apt-get install -y php5 apache2 php5-curl
cp -r www/ /var/www/html
rm /var/www/html/index.html
./etc/init.d/apache2 start
