#!/usr/bin/env bash

# TODO
# - Install flask server 
# - Install /vagrant/statscorona/requirements.txt
# - > export FLASK_APP=corona.py + export FLASK_ENV=development + flask run --host=<localip>
# - flask run -- does not work ? check why ! 

ctid=$(buildah from centos:centos8)

# Get all updates and install required packages
buildah run "$ctid" -- yum -y update
buildah run "$ctid" -- yum -y install git python3-pip python2-pip jq mlocate nc net-tools
buildah run "$ctid" -- updatedb
buildah run "$ctid" -- ln -s /usr/bin/pip3.6 /usr/bin/pip 
buildah run "$ctid" -- pip install --upgrade pip
buildah run "$ctid" -- pip install wheel pipenv       #  && pip3 install pipenv

# Set workingdir & copy app /vagrant to container
buildah copy "$ctid" "/vagrant" "/vagrant"
buildah config --workingdir "/vagrant/statscorona" "$ctid"

# Install flask and requirement
buildah run "$ctid" -- pip install flask
buildah run "$ctid" -- pip install -r /vagrant/statscorona/requirements.txt
buildah config --env FLASK_APP=/vagrant/statscorona/corona.py "$ctid" 
buildah config --env FLASK_ENV=development "$ctid"  
buildah config --entrypoint "flask run" "$ctid"
buildah config --port 5000 "$ctid"  
# buildah config --port 5000:5000 "$ctid"  
buildah run "$ctid" -- flask run --host=0.0.0.0 &
