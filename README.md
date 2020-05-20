# Build the docker container
sudo docker build --network=host -t coronaflask:latest /vagrant/
sudo docker run --net=host coronaflask:latest

# curl query commands
curl http://127.0.0.1:5000/getcountrylist
curl http://127.0.0.1:5000/getcoronapercountry/france
