from chalice import Chalice
from colorama import Fore

from chalicelib.helper import hello

app = Chalice(app_name='hello')


@app.route('/')
def index():
    return hello()


@app.route('/red/{name}')
def add(name: str):
    return f'{Fore.RED}{name}'
