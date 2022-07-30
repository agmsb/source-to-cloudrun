from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_label():
    release_value = os.environ.get('RELEASE')
    message = 'You are accessing the {version} version of the app! \n'.format(version=release_value)
    return(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
