FROM pramttl/ubuntu-python

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git
# Make ssh dir
RUN mkdir /root/.ssh/

# Copy over private key, and set permissions
ADD id_rsa  /root/.ssh/id_rsa

# Create known_hosts
RUN touch /root/.ssh/known_hosts

# Add bitbuckets key
RUN ssh-keyscan -T 60 172.16.15.205 >> /root/.ssh/known_hosts


# Clone the conf files into the docker container
RUN cd /root && \
    git clone git@172.16.15.205:ainvr/color-detection.git

RUN sudo apt-get -y install python-opencv libopencv-dev python-numpy python-dev

RUN sudo pip install matplotlib apscheduler==2.1.2 Pillow
