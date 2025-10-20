import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

print("🔍 FINAL INTELLIGENCE TEST")
print("=" * 35)

try:
    # Import directly from modules
    from modules.reconnaissance import whois_lookup, dns_enumeration
    print("✅ SUCCESS: Functions imported!")
    
    # Test with example.com
    print("\n1. Testing WHOIS lookup...")
    result = whois_lookup("example.com")
    print(f"   Result type: {type(result)}")
    
    print("\n2. Testing DNS enumeration...")
    result = dns_enumeration("example.com") 
    print(f"   Result type: {type(result)}")
    
    print("\n🎯 PROJECT SPHINX IS OPERATIONAL!")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print(f"Python path: {sys.path}")