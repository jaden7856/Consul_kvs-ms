import consul

c = consul.Consul()

c.kv.put('key1', 'bar')

