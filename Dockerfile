# Defining build tags
ARG base_image=python
ARG base_tag=3.12
# Possible classification is public_release public_test private_release private_test
ARG classification=public_release

# Exposing the port
EXPOSE 80

# Pull the image
FROM ${base_image}:${base_tag}

# Setting up the envionment 
WORKDIR /opt
COPY . /opt
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

# Running the release
CMD ["fastapi", "run", "app.py", "--port", "80"]
