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

def display_cep_intel(j):
    resultado = j.get('data', {})
    
    print(f"\n{Colors.PURPLE}=== [ GEASS CEP - GEOGRAPHIC LOGISTICS ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!] Geass failed with CEP search.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS CEP - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def cep_lookup(cep):
    url = "https://xbuscas.net/api/marketplace/v1/products/cep-credilink/consult"
    
    target = ''.join(filter(str.isdigit, cep))
    
    params = {
        "input": target,
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] GEOGRAPHIC KNOT ACQUISITION: {target}...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=20)
        
        if response.status_code == 200:
            display_cep_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Falha na autenticação do Token.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code}: Falha no banco de dados Credilink.{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Sincronização: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cep_lookup(sys.argv[1])
    else:
        print(f"{Colors.RED}[!] Erro: Informe o CEP para consulta.{Colors.RESET}")
