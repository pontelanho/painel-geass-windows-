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

def display_tel_intel(j):
    resultado = j.get('data', {})
    
    print(f"\n{Colors.PURPLE}=== [ GEASS PHONE - FULL DATA STREAM ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!] O Oráculo não encontrou registros para este número.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS PHONE - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f"Status Upstream: {j.get('upstream_status')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def tel_lookup(tel):
    url = "https://xbuscas.net/api/marketplace/v1/products/telefone/consult"
    
    tel_clean = ''.join(filter(str.isdigit, tel))
    
    params = {
        "input": tel_clean,
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] SCRAPPING DATA OUT OF THE PHONE: {tel_clean}...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=25)
        
        if response.status_code == 200:
            display_tel_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Token inválido ou revogado.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code}: Falha na comunicação com o Marketplace.{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Transmissão: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tel_lookup(sys.argv[1])
    else:
        print(f"{Colors.RED}[!] Erro: Informe o telefone (DDD + Número).{Colors.RESET}")
