   

from scapy.all import *


pacote = IP(dst="8.8.8.8")/ICMP()


resposta = sr1(pacote, timeout=2)



if resposta:
    resposta.show()

else:
    print("Sem resposta")




    import requests

    url = "httpp://httpbin.org/get"
    resposta = requests.get(url)

    print("Status", resposta.status_code)
    print