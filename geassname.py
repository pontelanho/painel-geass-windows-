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

def display_placa_intel(j):
    resultado = j.get('data', {})
    
    print(f"\n{Colors.PURPLE}=== [ GEASS NAME - PERSON TRACKER ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!] Geass hasn't found data for this person.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS NAME - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def placa_lookup(placa):
    url = "https://xbuscas.net/api/marketplace/v1/products/credlink/consult"
    
    target = placa.replace("-", "").replace(" ", "").upper()
    
    params = {
        "input": target,
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] THEY SHOUDNT'VE TOLD U THEIR NAME: {target}...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=30)
        
        if response.status_code == 200:
            display_placa_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Token recusado pelo sistema.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code}: Falha na consulta de nome.{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Sincronização: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        placa_lookup(sys.argv[1])
    else:
        print(f"{Colors.RED}[!] Erro: Informe o nome completo.{Colors.RESET}")
