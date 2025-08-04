# Defining build tags
ARG base_image=python
ARG base_tag=3.12
# Possible classification is public_release public_test private_release private_test
ARG classification=public_release
ARG work_dir /opt/batbmp
ARG port_number=80

# Passing to the container
ENV base_image=$base_image
ENV base_tag=$base_tag
ENV classification=$classification
ENV work_dir=$work_dir
ENV port_number=$port_number

# Exposing the port
EXPOSE $port_number

# Pull the image
FROM ${base_image}:${base_tag}

# Setting up the envionment 
RUN mkdir -p $work_dir
COPY . $work_dir
WORKDIR $work_dir
RUN python -m pip install -r requirements.txt

# Running the release
CMD ["fastapi", "run", "app.py", "--port", "$port"]
