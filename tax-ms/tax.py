from flask import Flask
import requests
import os
 
app = Flask(__name__)

# tax.py &
@app.route('/')
def get_tax():
    ver="1.0"
    res='{"Service":"Tax", "Version":' + ver + '}\n'
    return res
 
if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    app.run()