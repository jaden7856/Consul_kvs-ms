from flask import Flask
import requests
import os
 
import consul

app = Flask(__name__)

# TAX_SVC_URL=http://localhost:5002 python invoice.py &
@app.route('/')
def get_invoice():
    # url=os.environ.get('TAX_SVC_URL')
    client = consul.Consul(host='10.5.0.2', port=8500)

    serviceName = "tax-ms"
    # service_address = client.catalog.service(serviceName)[1][0]['ServiceAddress']
    # service_port = client.catalog.service(serviceName)[1][0]['ServicePort']
    # Proxy IP로 접속해야 Intentio으로 제어 가능
    service_address = "127.0.0.1"
    service_port = 16002

    url = "http://{}:{}".format(service_address, service_port)

    response = requests.get(url)
    ver="1.0"
    res='{"Service":"Invoice", "Version":' + ver + '}\n'
    res=res + response.content.decode('utf-8')
    return res
 
if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    app.run()