import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN = "INSIRA SEU TOKEN PESSOAL AQUI"

class Colors:
    PURPLE = '\033[1;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    RED = '\033[1;31m'
    RESET = '\033[0m'

def display_titulo_intel(j):
    resultado = j.get('data', [])
    
    print(f"\n{Colors.PURPLE}=== [ GEASS TITLE - CIVIL REGISTRY ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!] Nenhum registro de Título Eleitoral encontrado.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS TITLE - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f"Requests Restantes: {j.get('api_info', {}).get('requests_remaining')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def titulo_lookup(titulo):
    url = "https://xbuscas.net/api/marketplace/v1/products/titulo/consult"
    
    titulo_clean = ''.join(filter(str.isdigit, titulo))
    
    params = {
        "input": titulo_clean,
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] ACCESSING DATABASE: {titulo_clean}...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=25)
        
        if response.status_code == 200:
            display_titulo_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Token inválido ou permissão negada.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code}: Falha no Oráculo.{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Sincronização: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        titulo_lookup(sys.argv[1])
    else:
        print(f"{Colors.RED}[!] Erro: Informe o número do Título de Eleitor.{Colors.RESET}")
