HOSTNAME="shard-2"

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

mongo 192.168.16.107:27017 -u mongo-admin -ppassword --authenticationDatabase admin --eval 'sh.addShard( "192.168.16.108:27017" );sh.addShard( "192.168.16.109:27017" )'

mongo 192.168.16.107:27017/ramen_rating -u mongo-admin -ppassword --authenticationDatabase admin --eval 'sh.enableSharding("ramen_rating")'

mongo 192.168.16.107:27017/ramen_rating -u mongo-admin -ppassword --authenticationDatabase admin --eval 'db.ratings.ensureIndex( { _id : "hashed" } ); sh.shardCollection( "ramen_rating.ratings", { "_id" : "hashed" } )'

mongoimport -h 192.168.16.107:27017 -d ramen_rating -c ratings -u mongo-admin -ppassword --authenticationDatabase admin --type csv --file /vagrant/sources/ramen-ratings.csv --headerline