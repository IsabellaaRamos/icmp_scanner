   

from scapy.all import *


pacote = IP(dst="8.8.8.8")/ICMP()


resposta = sr1(pacote, timeout=2)



if resposta:
    resposta.show()

else:
    print("Sem resposta")