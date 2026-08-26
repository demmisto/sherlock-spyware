# 🕵️ Spyware Agent - Surveillance Toolkit

> **⚠️ WARNING:** This tool is for **educational purposes only**. Unauthorized monitoring of computer activity without explicit consent is illegal and unethical. Use responsibly and only on systems you own or have explicit permission to monitor.

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/yourusername/spyware-agent)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)

## 🎯 Overview

A modular surveillance system that captures and transmits user activity data through webhooks. Built with Python, it combines keylogging and screenshots into a stealthy monitoring solution.

## ✨ Features

### 🔑 **Keylogging Module** (`karm`)
- Real-time keystroke capture using `pynput`
- Logs all keyboard activity to local file
- Seamless background operation

### 📸 **Screenshot Module** (`netra`)
- Periodic screen captures at configurable intervals
- Automatic PNG compression and formatting
- Timestamped filenames for easy tracking

### 📤 **Data Transmission** (`astra`)
- Automatic upload of captured data to webhook endpoint
- Supports both keylogs and screenshots
- Configurable upload intervals

### 🧵 **Multi-threaded Architecture**
- All modules run concurrently
- Non-blocking operations
- Daemon threads for clean shutdown

## 🚀 Installation

### Prerequisites
```bash
Python 3.6 or higher
pip package manager
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

**Requirements.txt:**
```
pynput==1.7.6
pyautogui==0.9.54
requests==2.28.2
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/spyware-agent.git
cd spyware-agent
```

## ⚙️ Configuration

### Webhook Setup
Update the `WEBHOOK_URL` variable in the script:
```python
WEBHOOK_URL = "YOUR_WEBHOOK_ENDPOINT_HERE"
```
> **Note:** Default uses webhook.site for testing - replace with your own endpoint for production use.

### Adjustable Parameters
```python
CAPTURE_INTERVAL = 10  # Screenshot interval (seconds)
KEYLOG_FILE = "patra.txt"  # Log file location
```

## 🎮 Usage

### Run the Agent
```bash
python spyware.py
```

### Expected Output
```
Starting surveillance agent...
[Screenshot] Sent: 200
[Keylog] Sent: 200
```

## 📁 File Structure
```
spyware-agent/
├── spyware.py          # Main application
├── patra.txt          # Keylog storage (auto-generated)
├── requirements.txt   # Dependencies
└── README.md         # Documentation
```

## 🛠️ How It Works

### Architecture Flow
```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Keylogger │────▶│   Log File   │────▶│                 │
│   (karm)    │     │  (patra.txt) │     │   Webhook       │
└─────────────┘     └──────────────┘     │   Endpoint      │
                                          │                 │
┌─────────────┐     ┌──────────────┐     │                 │
│  Screenshot │────▶│   PNG Image  │────▶│   (Upload)      │
│   (netra)   │     │  (In Memory) │     │                 │
└─────────────┘     └──────────────┘     └─────────────────┘
```

### Threading Model
1. **Main Thread** - Keeps application alive
2. **Keylogger Thread** - Captures keyboard input
3. **Screenshot Thread** - Captures screen at intervals  
4. **Upload Thread** - Sends data to webhook

## 🔒 Ethical Considerations

**Before using this tool, ensure you:**

✅ Have explicit written permission from system owners  
✅ Are using it on systems you personally own  
✅ Are compliant with local laws and regulations  
✅ Have informed users of monitoring activities  
✅ Are using it for legitimate security testing  

**Never use this for:**
❌ Spying on colleagues without consent  
❌ Monitoring family members without knowledge  
❌ Stealing passwords or personal information  
❌ Any illegal or unethical activities  

## 🧪 Testing

### Test with Webhook.site
1. Visit [webhook.site](https://webhook.site)
2. Get your unique URL
3. Update `WEBHOOK_URL` with your test endpoint
4. Run the script
5. Check webhook.site for incoming data

## ⚠️ Limitations

- Screenshot capture doesn't include mouse cursor
- Keylog format includes special key identifiers
- Requires internet connection for webhook transmission
- Python dependencies must be pre-installed

## 🔧 Troubleshooting

### Common Issues

**Module not found errors:**
```bash
pip install pynput pyautogui requests
```

**Permission denied on keylog:**
- Run with appropriate permissions
- Ensure file write access in current directory

**Webhook timeout:**
- Check internet connection
- Verify webhook endpoint is accessible

## 📊 Performance Impact

- **CPU Usage:** ~1-5% average  
- **Memory Usage:** ~20-40MB  
- **Network:** Periodic data transmission  
- **Storage:** ~500KB per screenshot  

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [pynput](https://github.com/moses-palmer/pynput) - Keyboard input handling
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Screenshot functionality
- [Requests](https://requests.readthedocs.io/) - HTTP communication

---

**Remember:** With great power comes great responsibility. Use this tool ethically and legally.

**Star ⭐ this repo if you find it educational!**
