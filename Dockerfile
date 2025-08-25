# Defining build tags
ARG base_image=registry.gitlab.com/monkeyboy107/python
ARG base_tag=1.0.1
# Possible classification is public_release public_test private_release private_test
ARG classification=public_release

# Pull the image
FROM ${base_image}:${base_tag}

# Exposing the port
EXPOSE 80

# Setting up the envionment 
RUN apt-get update
RUN apt-get install vim -y
ENV EDITOR=vim
WORKDIR /opt
COPY . /opt
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

# Running the release
CMD ["fastapi", "run", "app.py", "--port", "80"]
