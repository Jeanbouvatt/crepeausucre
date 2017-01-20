mkdir -p ~/lab
cd ~/lab
wget ftp://ftp.hpintelco.net/pub/openvpn/ca.crt
wget ftp://ftp.hpintelco.net/pub/openvpn/lab8.key
wget ftp://ftp.hpintelco.net/pub/openvpn/lab8.crt
wget ftp://ftp.hpintelco.net/pub/openvpn/vpnlab8.conf
sudo openvpn --config vpnlab8.conf
