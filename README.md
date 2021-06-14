$ consul.d 폴더의 json 파일을 "connect" 항목 없이 실행 
consul agent -dev -ui -dawtacenter zone1 -node host1 -config-dir ./consul.d/
python tax.py &
TAX_SVC_URL=http://tax.service.consul:5002 python invoice.py
INV_SVC_URL=http://invoice.service.consul:5001 python order.py &

dig @127.0.0.1 -p 8600 order.service.consul SRV
curl http://localhost:8500/v1/catalog/service/order

$ consul.d 폴더의 json 파일을 "connect" 항목 추가하여 실행 

consul connect proxy -sidecar-for order & 
consul connect proxy -sidecar-for invoice & 
consul connect proxy -sidecar-for tax & 

python tax.py &
TAX_SVC_URL=http://tax.service.consul:16002 python invoice.py
INV_SVC_URL=http://invoice.service.consul:16001 python order.py &