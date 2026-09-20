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

def display_full_intel(j):
    resultado = j.get('data', {})
    
    print(f"\n{Colors.PURPLE}=== [ GEASS CPF - FULL DATA STREAM ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!]  Verifique o input.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS CPF - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def cpf_lookup(cpf):
    url = "https://xbuscas.net/api/marketplace/v1/products/cpf-1/consult"
    
    params = {
        "input": cpf,
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] SYNCHRONIZING...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=25)
        
        if response.status_code == 200:
            display_full_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Token inválido ou saldo zerado.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code} no Oráculo.{Colors.RESET}")
            print(f"Resposta bruta: {response.text}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Conexão: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = ''.join(filter(str.isdigit, sys.argv[1]))
        cpf_lookup(target)
    else:
        print(f"{Colors.RED}[!] Erro: Provide Geass with CPF.{Colors.RESET}")
