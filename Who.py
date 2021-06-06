import whois
import pyfiglet
import os

os.system("clear")
os.system("mihawk")

#usei o comando do pyfliget pra fazer um ascii do que ta no parentesses
ascii_banner = pyfiglet.figlet_format("Whois?")
print(ascii_banner)

#perguntei o alvo e usei o whois.whois pra fazer a pesquisa baseado na resposta do "alvo"
alvo = input("alvo: ")
consulta = whois.whois(alvo)

#printei a consulta pra mostrar o resultado mais usei o .text 
print(consulta.text)
