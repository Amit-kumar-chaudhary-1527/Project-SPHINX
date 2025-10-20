import sys
import os

print("🔍 PROJECT SPHINX - ENVIRONMENT TEST")
print("=" * 40)

# Check virtual environment
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("✅ Virtual Environment: ACTIVE")
else:
    print("❌ Virtual Environment: INACTIVE")

# Check Python version
print(f"✅ Python Version: {sys.version}")

# Check current directory
print(f"✅ Working Directory: {os.getcwd()}")

print("\n🎯 STATUS: READY FOR INTELLIGENCE MODULE DEVELOPMENT")