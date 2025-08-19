   

from scapy.all import *

# Cria um pacote ICMP (ping) para o IP de teste
pacote = IP(dst="8.8.8.8")/ICMP()

# Envia e recebe respostas
resposta = sr1(pacote, timeout=2)


# Mostra a resposta
if resposta:
    resposta.show()

else:
    print("Sem resposta")




    import requests

    url = "httpp://httpbin.org/get"
    resposta = requests.get(url)

    print("Status", resposta.status_code)
    print("Comando", resposta.text[:200])  #Mostra só os 200 primeiros caracteres