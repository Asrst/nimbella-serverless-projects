# This will pull the official Gitpod `vnc` image
# which has much of what you need to start
FROM gitpod/workspace-full

USER root

RUN wget https://nimbella.io/downloads/nim/nim-install-linux.sh

RUN bash nim-install-linux.sh

USER gitpod

# RUN pip3 install -r requirements.txt

