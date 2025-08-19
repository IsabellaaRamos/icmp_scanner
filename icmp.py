
from scapy.all import sr1, IP, ICMP

print(" Testando scanner ICMP...")


alvo = "8.8.8.8"
pacote = IP(dst=alvo)/ICMP()


resposta = sr1(pacote, timeout=2, verbose=0)

if resposta:
    print(f"✅ O host {alvo}  respondeu ao ping!")

else:
    print(f"❌ O host {alvo}  não respondeu ao ping!")

    

