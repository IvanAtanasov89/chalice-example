# chalice-example

Deploys a lambda with http endpoint with very little code or config.

Prerequisites:

- Have Python 3.7 installed (can use pyenv)
- Have an AWS profile setup with credentials for a user that has permissions for deploying a lambda
- Have a default region set in environment var or within ~/.aws/config


```shell
pipenv install --dev
pipenv lock --requirements
pipenv run chalice deploy --profile profile_name
```
