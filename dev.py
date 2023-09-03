import requests

def obter_geolocalizacao(ip):
    url = f"https://ipinfo.io/{ip}/json"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("city", "Desconhecida")
        regiao = dados.get("region", "Desconhecida")
        pais = dados.get("country", "Desconhecido")
        org = dados.get("org", "Desconhecida")
        
        print(f"IP: {ip}")
        print(f"Cidade: {cidade}")
        print(f"Região: {regiao}")
        print(f"País: {pais}")
        print(f"Organização: {org}")
    else:
        print(f"Não foi possível obter informações para o IP {ip}")

if __name__ == "__main__":
    ip_alvo = input("Digite o endereço IP que você deseja consultar: ")
    obter_geolocalizacao(ip_alvo)
