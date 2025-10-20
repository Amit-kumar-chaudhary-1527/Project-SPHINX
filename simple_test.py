import os
import importlib.util

print("🔍 SIMPLE MODULE TEST")
print("=" * 30)

# Check if we can load the module directly
module_path = os.path.join('modules', 'reconnaissance.py')
if os.path.exists(module_path):
    print("✅ reconnaissance.py exists")
    
    # Try to import the module
    try:
        spec = importlib.util.spec_from_file_location("reconnaissance", module_path)
        recon_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(recon_module)
        
        # Check if functions exist
        if hasattr(recon_module, 'whois_lookup'):
            print("✅ whois_lookup function found")
        else:
            print("❌ whois_lookup function NOT found")
            
        if hasattr(recon_module, 'dns_enumeration'):
            print("✅ dns_enumeration function found")
        else:
            print("❌ dns_enumeration function NOT found")
            
    except Exception as e:
        print(f"❌ Error loading module: {e}")
else:
    print("❌ reconnaissance.py not found")