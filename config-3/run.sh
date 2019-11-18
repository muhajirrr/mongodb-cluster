HOSTNAME="config-3"

# Install MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

sudo apt-get update
sudo apt-get install -y mongodb-org

sudo service mongod start
sleep 5s

# Set Up MongoDB Authentication

## Copy a Key file
sudo mkdir /opt/mongo
sudo cp /vagrant/sources/mongo-keyfile /opt/mongo/mongo-keyfile
sudo chmod 400 /opt/mongo/mongo-keyfile
sudo chown mongodb:mongodb /opt/mongo/mongo-keyfile

sudo cp "/vagrant/$HOSTNAME/mongod.conf" /etc/mongod.conf

sudo systemctl restart mongod
sleep 5s

mongo 192.168.16.104:27019 -u mongo-admin -ppassword --authenticationDatabase admin --eval 'rs.initiate( { _id: "configReplSet", configsvr: true, members: [ { _id: 0, host: "192.168.16.104:27019" }, { _id: 1, host: "192.168.16.105:27019" }, { _id: 2, host: "192.168.16.106:27019" } ] } )'