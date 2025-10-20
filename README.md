# 🔍 Project Sphinx - Advanced Intelligence Gathering System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

A professional-grade Open Source Intelligence (OSINT) framework designed for cybersecurity professionals, penetration testers, and intelligence operations. Project Sphinx automates the collection and correlation of critical intelligence from multiple sources.

## 🎯 Project Vision

> "In the realm of cybersecurity, knowledge is the ultimate weapon. Project Sphinx represents my commitment to advancing India's cyber intelligence capabilities and contributing to national security."

**Developer:** Amit Kumar Chaudhary | **BTech Cybersecurity Student**  
**Goal:** To develop advanced tools for intelligence agencies and cyber defense operations

## 🚀 Core Capabilities

### 🔎 Multi-Source Intelligence Integration
- **WHOIS Intelligence**: Comprehensive domain registration analysis
- **DNS Infrastructure Mapping**: Complete network reconnaissance
- **Shodan Vulnerability Assessment**: Real-time threat intelligence
- **Automated Correlation**: Intelligent data cross-referencing

### 📊 Advanced Reporting
- **Structured JSON Reports**: Machine-readable intelligence data
- **Executive Summaries**: Actionable intelligence insights
- **Timeline Analysis**: Historical intelligence tracking
- **Professional Documentation**: Enterprise-grade reporting

## 🛠️ Technical Architecture

### 🏗️ System Architecture
Project Sphinx follows a modular architecture designed for scalability and extensibility:
project-sphinx/
├── 🎯 sphinx_core.py # Main Intelligence Engine
├── 📁 modules/ # Intelligence Modules
│ ├── reconnaissance.py # WHOIS & DNS Intelligence
│ └── shodan_intel.py # Vulnerability Assessment
├── 📊 reports/ # Intelligence Output
├── 🔧 requirements.txt # Dependencies
└── 📚 README.md # Documentation

text

### 🔧 Core Modules

#### 🎯 Intelligence Engine (`sphinx_core.py`)
- **Orchestration Layer**: Coordinates all intelligence gathering operations
- **Report Generation**: Automated JSON intelligence reporting
- **Command Line Interface**: Professional user interaction
- **Error Handling**: Robust exception management

#### 🔍 Reconnaissance Module (`modules/reconnaissance.py`)
- **WHOIS Intelligence**: Domain registration analysis, ownership tracing, expiration monitoring
- **DNS Enumeration**: A records, MX records, NS records, TXT records analysis
- **IP Resolution**: Domain-to-IP mapping for further intelligence
- **Infrastructure Mapping**: Complete network footprint analysis

#### 🛡️ Shodan Intelligence (`modules/shodan_intel.py`)
- **Vulnerability Assessment**: CVE detection and risk analysis
- **Service Discovery**: Open port scanning and service identification
- **Banner Grabbing**: Service version and configuration intelligence
- **Threat Correlation**: Multi-source intelligence integration

## 💻 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Shodan API key (for vulnerability intelligence - optional but recommended)

### Quick Start
```bash
#Clone the repository
git clone https://github.com/Amit-kumar-chaudhary-1527/Project-SPHINX.git
cd Project-SPHINX

# Create virtual environment
python -m venv sphinx_env
sphinx_env\Scripts\activate  # Windows
# OR
source sphinx_env/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set up Shodan API (optional)
set SHODAN_API_KEY=your_api_key_here  # Windows
# OR
export SHODAN_API_KEY=your_api_key_here  # Linux/Mac
🚀 Usage Examples
Basic Intelligence Gathering
bash
python sphinx_core.py -t example.com -o reports
Advanced Operations
bash
# With Shodan vulnerability assessment
python sphinx_core.py -t target.com -o reports --shodan-key YOUR_API_KEY

# Multiple target analysis
python sphinx_core.py -t github.com -o reports
python sphinx_core.py -t microsoft.com -o reports
Command Line Arguments
-t, --target - Target domain (required)

-o, --output - Output directory (default: reports)

-s, --shodan-key - Shodan API key for enhanced intelligence

📊 Sample Intelligence Output
json
{
  "target": "example.com",
  "timestamp": "2025-10-20T15:40:07.165703",
  "whois": {
    "registrar": "RESERVED-Internet Assigned Numbers Authority",
    "creation_date": "1995-08-14 04:00:00+00:00",
    "name_servers": ["A.IANA-SERVERS.NET", "B.IANA-SERVERS.NET"]
  },
  "dns": {
    "a_records": ["93.184.216.34"],
    "mx_records": ["0 ."],
    "txt_records": ["v=spf1 -all"]
  }
}
⚠️ Legal & Ethical Usage
Important: Project Sphinx is designed for:

Authorized penetration testing

Security research with proper permissions

Educational purposes

Legitimate cybersecurity operations

Never use this tool on systems you don't own or without explicit written permission.

🔮 Future Enhancements
Dark web intelligence integration

Social media footprint analysis

Advanced threat intelligence feeds

Machine learning for pattern recognition

Real-time monitoring capabilities

🤝 Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for discussion.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Shodan for vulnerability intelligence API

Python community for excellent libraries

Cybersecurity mentors for guidance and inspiration

🔍 Project Sphinx - Advancing cyber intelligence capabilities for a secure digital India. 🛡️

Developer: Amit Kumar Chaudhary | BTech Cybersecurity | Aspiring Intelligence 
