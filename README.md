# Build the docker container <br />
sudo docker build --network=host -t coronaflask:latest /vagrant/ <br />
sudo docker run --net=host coronaflask:latest <br />

# curl query commands <br />
curl http://127.0.0.1:5000/getcountrylist <br />
curl http://127.0.0.1:5000/getcoronapercountry/france <br />
