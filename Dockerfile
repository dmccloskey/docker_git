# Dockerfile to build git repositories

# Set the base image
FROM debian:latest

# File Author / Maintainer
LABEL maintainer Douglas McCloskey <dmccloskey87@gmail.com

# Create a User
ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
    && chmod -R u+rwx $HOME \
    && chown -R user:user $HOME

# Install GitHub
RUN apt-get update && apt-get upgrade -y \
	&& apt-get install -y \
	git \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir /home/user/GitHub

# Clone GitHub repos
COPY Git/git.py /home/user/GitHub/git.py
COPY Git/repositories.csv /home/user/GitHub/repositories.csv
	
WORKDIR $HOME
USER user

#docker run -d -v //C/Users/domccl/Desktop/GitHub:/home/user/GitHub