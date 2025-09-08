# Run
## Prod
```
docker run -v /etc/batbmp/:/etc/batbmp/ -v /var/batbmp/:/var/batbmp/ -p 80:80 --restart=always --name batbmp -it -d registry.gitlab.com/batbmp/batbmp:latest
```
## Dev
```
python -m fastapi dev app.py
```
# Workflow
At the end of the day, rebase from `main`

## Rebasing
When you are ready to merge code into `main` rebase `main` into current branch using the following
```
git checkout main
git pull
git rebase main YOUR_CURRENT_BRANCH
```

## Commit message format
[We use angular commit scheme](https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md)

## Contributing

### Development Environment
This project uses EL 9.3 as the assumed development environment.
To set up a development environment, follow these steps:

- Install `make` using your package manager if it's not already installed.
- Run `make setup` to create a virtual environment and install dependencies.
- Activate the virtual environment with `source venv/bin/activate`.
- Create a local `config.yaml` file by copying the example file `config.yaml.example`.
- Update the config.yaml to be what you want for your defaults
