from flask import Flask
import requests
import os

import consul
 
app = Flask(__name__)

# INV_SVC_URL=http://localhost:5001 python order.py &
@app.route('/')
def get_order():
    # url=os.environ.get('INV_SVC_URL')
    client = consul.Consul(host='10.5.0.2', port=8500)

    serviceName = "invoice-ms"
    service_address = client.catalog.service(serviceName)[1][0]['ServiceAddress']
    service_port = client.catalog.service(serviceName)[1][0]['ServicePort']

    url = "http://{}:{}".format(service_address, service_port)
    
    response = requests.get(url)
    ver="1.0"
    res='{"Service":"Order", "Version":' + ver + '}\n'
    res=res + response.content.decode('utf-8')
    return res
 
if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    app.run()
