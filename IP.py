import ipaddress

ip = "192.168.0.0/24"
iprede= "192.168.0.0"
rede = ipaddress.ip_network(ip,strict=False)
endereco = ipaddress.ip_address(iprede)

for ip in rede:
    print(ip)

print(rede)
print(endereco)