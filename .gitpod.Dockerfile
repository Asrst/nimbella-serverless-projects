# This will pull the official Gitpod `vnc` image
# which has much of what you need to start
FROM gitpod/workspace-full

USER gitpod

RUN wget https://nimbella.io/downloads/nim/nim-install-linux.sh

RUN sudo bash nim-install-linux.sh

# RUN pip3 install -r requirements.txt

