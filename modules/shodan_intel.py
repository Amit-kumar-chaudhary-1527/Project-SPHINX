import shodan
from datetime import datetime

class ShodanIntelligence:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            self.api = shodan.Shodan(api_key)
            print("[SHODAN] API initialized successfully")
        except Exception as e:
            print(f"[SHODAN] API initialization failed: {e}")
            self.api = None
        
    def host_intelligence(self, ip):
        """
        Gather intelligence on a specific IP address
        """
        if not self.api:
            return {'error': 'Shodan API not initialized', 'target_ip': ip}
            
        print(f"[SHODAN] Gathering intelligence for IP: {ip}")
        
        try:
            host_info = self.api.host(ip)
            
            intelligence = {
                'target_ip': ip,
                'organization': host_info.get('org', 'N/A'),
                'operating_system': host_info.get('os', 'N/A'),
                'ports': host_info.get('ports', []),
                'vulnerabilities': host_info.get('vulns', []),
                'services': [],
                'timestamp': datetime.now().isoformat()
            }
            
            # Extract service information
            for service in host_info.get('data', []):
                service_info = {
                    'port': service.get('port'),
                    'service': service.get('product', 'N/A'),
                    'version': service.get('version', 'N/A'),
                    'banner': service.get('banner', 'N/A')[:200] if service.get('banner') else 'N/A'
                }
                intelligence['services'].append(service_info)
            
            print(f"[SHODAN] Found {len(intelligence['ports'])} open ports")
            print(f"[SHODAN] Found {len(intelligence['services'])} services")
            if intelligence['vulnerabilities']:
                print(f"[SHODAN] Found {len(intelligence['vulnerabilities'])} potential vulnerabilities")
                
            return intelligence
            
        except shodan.APIError as e:
            print(f"[SHODAN] API Error: {e}")
            return {'error': str(e), 'target_ip': ip}
        except Exception as e:
            print(f"[SHODAN] Unexpected error: {e}")
            return {'error': str(e), 'target_ip': ip}