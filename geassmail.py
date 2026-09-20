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

def display_email_intel(j):
    resultado = j.get('data', {})
    
    print(f"\n{Colors.PURPLE}=== [ GEASS OMNISCIENT - EMAIL VINCULUM ] ==={Colors.RESET}")
    
    if not resultado:
        print(f"{Colors.RED}[!] Geass hasn't found any available data on this e-mail.{Colors.RESET}")
        return

    full_output = json.dumps(resultado, indent=4, ensure_ascii=False)
    for line in full_output.split('\n'):
        print(f"{Colors.CYAN}{line}{Colors.RESET}")
        
    print(f"\n{Colors.PURPLE}--- [ GEASS MAIL - FUEL INFO ] ---")
    print(f"Cost: {j.get('charged')} | Fuel: {j.get('balance_after')}")
    print(f'=== [ "If strength is justice, then is powerlessness a crime?" - Lelouch Vi Britannia ] ==={Colors.RESET}')

def email_lookup(email):
    url = "https://xbuscas.net/api/marketplace/v1/products/email/consult"
    
    params = {
        "input": email.strip().lower(),
        "token": TOKEN
    }

    print(f"\n{Colors.PURPLE}[!] TRACING DIGITAL FOOTPRINT: {email}...{Colors.RESET}")
    
    try:
        response = requests.get(url, params=params, verify=False, timeout=25)
        
        if response.status_code == 200:
            display_email_intel(response.json())
        elif response.status_code == 401:
            print(f"{Colors.RED}[!] ERRO 401: Token inválido. Verifique seu Perfil no XBuscas.{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Erro {response.status_code} na API.{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Falha Crítica na Sincronização: {e}{Colors.RESET}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        email_lookup(sys.argv[1])
    else:
        print(f"{Colors.RED}[!] Erro: Informe o e-mail alvo.{Colors.RESET}")
