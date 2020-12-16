#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

useradd --create-home --shell /bin/bash  --uid 1000 myname

apt-get update && apt-get install -y curl vim certbot dnsutils python3.8 python3-pip

echo "=== setup Timezone: Asia/Tokyo ==="
/usr/bin/unlink /etc/localtime/
/usr/bin/ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
date

echo "=== check python version ==="
ln -s /usr/bin/python3.8 /usr/bin/python
python -V
whereis -b python

echo "=== check pip version ==="
ln -s /usr/bin/pip3 /usr/bin/pip
pip -V
whereis -b pip

echo "=== Now installing pip3 modules ==="
pip3 install requests

echo "=== certbot status ==="
certbot --version
whereis -b certbot

echo "=== dnsutils status ==="
whereis -b nslookup
whereis -b dig
whereis -b nsupdate

echo "=== setup permission shell script files *.sh ==="
/usr/bin/chmod +x /data/*.sh
ls -al /data/*.sh
