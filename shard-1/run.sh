HOSTNAME="shard-1"

# Install MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

sudo apt-get update
sudo apt-get install -y mongodb-org

sudo service mongod start
sleep 5s

## Copy a Key file
sudo mkdir /opt/mongo
sudo cp /vagrant/sources/mongo-keyfile /opt/mongo/mongo-keyfile
sudo chmod 400 /opt/mongo/mongo-keyfile
sudo chown mongodb:mongodb /opt/mongo/mongo-keyfile

sudo cp "/vagrant/$HOSTNAME/mongod.conf" /etc/mongod.conf

sudo systemctl restart mongod
sleep 5s