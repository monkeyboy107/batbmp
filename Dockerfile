# Defining build tags
ARG base_image=registry.gitlab.com/monkeyboy107/python
ARG base_tag=1.0.6
# Possible classification is public_release public_test private_release private_test
ARG classification=public_release

# Pull the image
FROM ${base_image}:${base_tag}

# Exposing the port
EXPOSE 80

# Setting up the envionment 
RUN dnf install vim -y
ENV EDITOR=vim
COPY . /opt/batbmp
WORKDIR /opt/batbmp
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

# Running the release
CMD ["fastapi", "run", "app.py", "--port", "80"]
