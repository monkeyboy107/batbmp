# Defining build tags
ARG base_image=python
ARG base_tag=3.12
# Possible classification is public_release public_test private_release private_test
ARG classification=public_release
ARG work_dir /opt/

# Passing to the container
ENV base_image=$base_image
ENV base_tag=$base_tag
ENV classification=$classification
ENV work_dir=$work_dir

# Exposing the port
EXPOSE 80

# Pull the image
FROM ${base_image}:${base_tag}

# Setting up the envionment 
COPY . $work_dir
WORKDIR $work_dir
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
RUN echo $port_number

# Running the release
CMD ["fastapi", "run", "app.py", "--port", "80"]
