from flask import Flask
app = Flask(__name__)
@app.route('/’)
def hello_world():
return 'Hello, World!’
for cntr in range(0,10):
    print (cntr)
