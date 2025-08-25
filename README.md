# Setup
Run the following commands to setup your environment
```
make setup
source venv/bin/activate
cp config.yaml.example config.yaml
```
Update the config.yaml to be what you want for your defaults

# Run
## Prod
```
docker run -v /etc/batbmp/:/etc/batbmp/ -v /var/batbmp/:/var/batbmp/ -p 80:80 --restart=always --name batbmp -it -d registry.gitlab.com/monkeyboy107/batbmp:latest
```
## Dev
```
python -m fastapi dev app.py
```
