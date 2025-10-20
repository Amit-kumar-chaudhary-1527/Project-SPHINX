import os
from modules.shodan_intel import ShodanIntelligence
from modules.reconnaissance import get_ip_from_domain

# Replace with your actual Shodan API key
SHODAN_API_KEY = "YOUR_API_KEY_HERE"

def test_shodan():
    if SHODAN_API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Please add your Shodan API key to the script")
        return
        
    shodan_intel = ShodanIntelligence(SHODAN_API_KEY)
    
    # Test with a domain
    domain = "example.com"
    ip = get_ip_from_domain(domain)
    
    if ip:
        print(f"\n🔍 GATHERING SHODAN INTELLIGENCE FOR: {ip}")
        result = shodan_intel.host_intelligence(ip)
        
        if 'error' not in result:
            print(f"\n📊 SHODAN INTELLIGENCE SUMMARY:")
            print(f"   Organization: {result.get('organization', 'N/A')}")
            print(f"   Open Ports: {len(result.get('ports', []))}")
            print(f"   Services: {len(result.get('services', []))}")
            print(f"   Vulnerabilities: {len(result.get('vulnerabilities', []))}")
        else:
            print(f"   Error: {result['error']}")

if __name__ == "__main__":
    test_shodan()