from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_version():
    commit_sha = os.environ.get('COMMIT_SHA')
    if 'COMMIT_SHA' in os.environ:
        message = 'Hello from the revision of the app built by this commit: {COMMIT_SHA}! \n'.format(commit_sha=commit_sha)
    else:
        message = 'Hello - no current info on the commit that built this revision of the app.'
    return(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)