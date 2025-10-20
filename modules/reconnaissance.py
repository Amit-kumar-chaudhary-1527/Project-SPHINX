import whois
import socket
import dns.resolver
from datetime import datetime

def whois_lookup(domain):
    print(f"[WHOIS] Gathering intelligence for: {domain}")
    try:
        domain_info = whois.whois(domain)
        intelligence = {
            'target': domain,
            'registrar': domain_info.registrar,
            'creation_date': domain_info.creation_date,
            'expiration_date': domain_info.expiration_date,
            'name_servers': list(domain_info.name_servers) if domain_info.name_servers else [],
            'status': domain_info.status,
            'emails': domain_info.emails,
            'dnssec': domain_info.dnssec,
            'timestamp': datetime.now().isoformat()
        }
        print(f"[WHOIS] Intelligence gathered successfully")
        return intelligence
    except Exception as e:
        print(f"[WHOIS] ERROR: {str(e)}")
        return {'error': str(e), 'target': domain}

def dns_enumeration(domain):
    print(f"[DNS] Enumerating records for: {domain}")
    dns_intel = {
        'target': domain,
        'a_records': [],
        'mx_records': [],
        'ns_records': [],
        'txt_records': [],
        'subdomains': []
    }
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        dns_intel['a_records'] = [str(ip) for ip in a_records]
        mx_records = dns.resolver.resolve(domain, 'MX')
        dns_intel['mx_records'] = [str(mx) for mx in mx_records]
        ns_records = dns.resolver.resolve(domain, 'NS')
        dns_intel['ns_records'] = [str(ns) for ns in ns_records]
        txt_records = dns.resolver.resolve(domain, 'TXT')
        dns_intel['txt_records'] = [str(txt) for txt in txt_records]
        print(f"[DNS] Found {len(dns_intel['a_records'])} A records")
        print(f"[DNS] Found {len(dns_intel['mx_records'])} MX records")
    except Exception as e:
        print(f"[DNS] ERROR: {str(e)}")
        dns_intel['error'] = str(e)
    return dns_intel

def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[DNS] Resolved {domain} -> {ip}")
        return ip
    except socket.gaierror as e:
        print(f"[DNS] Resolution failed: {e}")
        return None
