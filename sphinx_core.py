#!/usr/bin/env python3
"""
PROJECT SPHINX - ADVANCED INTELLIGENCE GATHERING SYSTEM
Author: [Your Name]
Classification: INTERNAL USE ONLY
"""

import argparse
import json
import os
from datetime import datetime
from modules.reconnaissance import whois_lookup, dns_enumeration, get_ip_from_domain
from modules.shodan_intel import ShodanIntelligence

class SphinxIntelligence:
    def __init__(self, shodan_api_key=None):
        self.version = "1.2"
        self.intel_data = {}
        
        # Try to get Shodan key from environment if not provided
        if not shodan_api_key:
            shodan_api_key = os.getenv('SHODAN_API_KEY')
        
        self.shodan_api_key = shodan_api_key
        self.shodan_intel = None
        
        if shodan_api_key and shodan_api_key != "YOUR_API_KEY_HERE":
            self.shodan_intel = ShodanIntelligence(shodan_api_key)
        
    def print_banner(self):
        banner = """
    ███████ ██████  ██   ██ ███    ██ ██   ██
    ██      ██   ██ ██  ██  ████   ██ ██  ██ 
    ███████ ██████  █████   ██ ██  ██ █████  
         ██ ██      ██  ██  ██  ██ ██ ██  ██ 
    ███████ ██      ██   ██ ██   ████ ██   ██
    
        ADVANCED INTELLIGENCE GATHERING SYSTEM
        """
        print(banner)
        print(f"Version: {self.version} | Started: {datetime.now()}")
        if self.shodan_intel:
            print("🔍 Shodan Intelligence: ENABLED")
        else:
            print("⚠️  Shodan Intelligence: DISABLED (no API key)")
        print("=" * 60)

    def gather_intelligence(self, target):
        """Main intelligence gathering function"""
        print(f"\n🎯 TARGET: {target}")
        print("-" * 50)
        
        # Initialize target data
        self.intel_data[target] = {
            'timestamp': datetime.now().isoformat(),
            'target': target
        }
        
        # Phase 1: WHOIS Intelligence
        print("\n📋 PHASE 1: DOMAIN REGISTRATION INTELLIGENCE")
        whois_intel = whois_lookup(target)
        self.intel_data[target]['whois'] = whois_intel
        
        # Phase 2: DNS Intelligence  
        print("\n🌐 PHASE 2: DNS INFRASTRUCTURE INTELLIGENCE")
        dns_intel = dns_enumeration(target)
        self.intel_data[target]['dns'] = dns_intel
        
        # Phase 3: Shodan Intelligence (if available)
        if self.shodan_intel:
            print("\n🔍 PHASE 3: SHODAN VULNERABILITY INTELLIGENCE")
            ip_address = get_ip_from_domain(target)
            if ip_address:
                shodan_intel = self.shodan_intel.host_intelligence(ip_address)
                self.intel_data[target]['shodan'] = shodan_intel
            else:
                print("[SHODAN] Could not resolve IP address for Shodan lookup")
        
        print(f"\n✅ INTELLIGENCE GATHERING COMPLETE FOR: {target}")
        
    def generate_report(self, target, output_dir="reports"):
        """Generate intelligence report"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/sphinx_report_{target}_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.intel_data[target], f, indent=2, default=str)
            
        print(f"\n📊 INTELLIGENCE REPORT: {filename}")
        return filename

    def display_summary(self, target):
        """Display intelligence summary"""
        print(f"\n📈 INTELLIGENCE SUMMARY: {target}")
        print("=" * 50)
        
        data = self.intel_data[target]
        
        # WHOIS Summary
        whois_data = data.get('whois', {})
        print(f"\n📋 DOMAIN INTELLIGENCE:")
        print(f"   Registrar: {whois_data.get('registrar', 'N/A')}")
        print(f"   Created: {whois_data.get('creation_date', 'N/A')}")
        print(f"   Expires: {whois_data.get('expiration_date', 'N/A')}")
        print(f"   Name Servers: {len(whois_data.get('name_servers', []))}")
        
        # DNS Summary
        dns_data = data.get('dns', {})
        print(f"\n🌐 NETWORK INTELLIGENCE:")
        print(f"   IP Addresses: {len(dns_data.get('a_records', []))}")
        print(f"   Mail Servers: {len(dns_data.get('mx_records', []))}")
        print(f"   Name Servers: {len(dns_data.get('ns_records', []))}")
        print(f"   TXT Records: {len(dns_data.get('txt_records', []))}")
        
        # Shodan Summary
        shodan_data = data.get('shodan', {})
        if shodan_data and 'error' not in shodan_data:
            print(f"\n🔍 VULNERABILITY INTELLIGENCE:")
            print(f"   Organization: {shodan_data.get('organization', 'N/A')}")
            print(f"   Open Ports: {len(shodan_data.get('ports', []))}")
            print(f"   Services: {len(shodan_data.get('services', []))}")
            print(f"   Vulnerabilities: {len(shodan_data.get('vulnerabilities', []))}")
        elif self.shodan_intel:
            print(f"\n⚠️  Shodan: {shodan_data.get('error', 'No data')}")

def main():
    parser = argparse.ArgumentParser(description='Project Sphinx - Intelligence Gathering System')
    parser.add_argument('-t', '--target', required=True, help='Target domain for intelligence gathering')
    parser.add_argument('-o', '--output', default='reports', help='Output directory for reports')
    parser.add_argument('-s', '--shodan-key', help='Shodan API key for vulnerability intelligence')
    
    args = parser.parse_args()
    
    # Initialize Sphinx with Shodan
    sphinx = SphinxIntelligence(args.shodan_key)
    sphinx.print_banner()
    
    # Gather intelligence
    sphinx.gather_intelligence(args.target)
    
    # Generate report
    report_file = sphinx.generate_report(args.target, args.output)
    
    # Display summary
    sphinx.display_summary(args.target)
    
    print(f"\n🎯 MISSION COMPLETE: Intelligence gathered for {args.target}")
    print(f"📁 Report saved: {report_file}")

if __name__ == "__main__":
    main()