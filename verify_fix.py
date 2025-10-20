print("🔍 VERIFYING FIX")
print("=" * 20)

try:
    from modules.reconnaissance import get_ip_from_domain
    print("✅ SUCCESS: get_ip_from_domain imported!")
    
    # Test the function
    ip = get_ip_from_domain("google.com")
    print(f"✅ Function works! IP: {ip}")
    
    # Test other functions
    from modules.reconnaissance import whois_lookup, dns_enumeration
    print("✅ All functions imported successfully!")
    
except Exception as e:
    print(f"❌ ERROR: {e}")