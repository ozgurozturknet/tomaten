#add a skafold of the main.py file  
from flask import Flask

print "Merhaba Dunya"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()