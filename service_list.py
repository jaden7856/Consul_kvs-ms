import requests
import consul

client = consul.Consul(host='localhost', port=8500)

serviceName = "order-ms"
service_address = client.catalog.service(serviceName)[1][0]['ServiceAddress']
service_port = client.catalog.service(serviceName)[1][0]['ServicePort']

# request url
response = requests.get("http://{}:{}".format(service_address, service_port))
res = response.content.decode('utf-8')

print(res)


