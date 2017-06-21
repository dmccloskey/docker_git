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
	python3 \
	ca-certificates \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir /home/user/GitHub

# Clone GitHub repos
COPY Git/ /home/user/Git
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s /usr/local/bin/docker-entrypoint.sh / && chmod +x /usr/local/bin/docker-entrypoint.sh
	
WORKDIR $HOME
USER user

CMD ["docker-entrypoint.sh"]

##EXAMPLE USAGE:
#docker build -t dmccloskey/docker-git .
#docker run -d -v //C/Users/domccl/Desktop/GitHub:/home/user/GitHub --name=git dmccloskey/docker-git
#docker run -d -v //C/Users/dmccloskey/Documents/GitHub:/home/user/GitHub --name=git dmccloskey/docker-git
#docker exec -it git /bin/bash
#python3
#from Git.Git import Git
#git = Git(email='dmccloskey87@gmail.com',username='dmccloskey',password='',repositories_csv='Git/repositories.csv')
#git.make_sslCert()
#git.clone_repositories()