import os
import sys

print("🔍 DEBUG SHODAN MODULE")
print("=" * 25)

# Check if file exists
shodan_file = os.path.join('modules', 'shodan_intel.py')
print(f"File exists: {os.path.exists(shodan_file)}")

if os.path.exists(shodan_file):
    # Read and display first 10 lines
    with open(shodan_file, 'r') as f:
        lines = f.readlines()
        print(f"File has {len(lines)} lines")
        print("\nFirst 10 lines:")
        for i, line in enumerate(lines[:10], 1):
            print(f"{i:2}: {line.rstrip()}")
    
    # Try to import
    try:
        from modules.shodan_intel import ShodanIntelligence
        print("\n✅ SUCCESS: ShodanIntelligence imported!")
    except ImportError as e:
        print(f"\n❌ IMPORT ERROR: {e}")
else:
    print("❌ shodan_intel.py not found!")