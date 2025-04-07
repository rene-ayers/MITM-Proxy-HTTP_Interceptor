# HTTP Traffic Interceptor with mitmproxy

This Python tool works with **mitmproxy** to capture and log HTTP/HTTPS traffic. It prints each request's method and URL to the terminal, saves details to a `.log` file for quick viewing, and writes full request data to a `.json` file for deeper analysis.

---

## Features

- Captures all HTTP(S) requests in real-time
- Logs the following:
  - Host
  - URL
  - Method (GET, POST, etc.)
  - Request headers
- Saves data to:
  - `http_traffic.log` (human-readable log)
  - `traffic_data.json` (structured JSON format)
- Easy to run with mitmproxy

---

## File Descriptions

| File Name              | Purpose                                 |
|------------------------|-----------------------------------------|
| `traffic_logger.py`    | Python script used with mitmproxy       |
| `http_traffic.log`     | Log file with basic request details     |
| `traffic_data.json`    | JSON file with full request metadata    |
| `install.txt`          | Instructions for setting up mitmproxy   |

---

## How to Setup and Use the Tool

1. **Install mitmproxy**

   Open your terminal and run:

   ```bash
   pip install mitmproxy

2. Save the Python script
  - Create a file named `traffic_logger.py`. 
  - Paste the script code into this file and save it.

3. Run **mitmproxy** with your script
  - In your terminal, navigate to the folder where `traffic_logger.py` is saved and run:
    mitmproxy -s traffic_logger.py
 
4. Set up your browser or device to use **mitmproxy** 
  - Open your browser or device’s proxy settings
  - Set the proxy to: 
      - Address: 127.0.0.1
      - Port: 8080

5. Browse the internet
  - Go to websites like Google.com
  - Your termnal will display traffic
  - The tool will:
      - Print each request
      - Log requests to `http_traffic.log`
      - Save detailed data to `traffic_data.json`

**This tool is for educational and authorized use only. Do not monitor without consent or permission.**
