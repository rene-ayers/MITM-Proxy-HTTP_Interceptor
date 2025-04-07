import json
import logging
from mitmproxy import ctx

# See install.txt for help setting up

# Setup logging
log_file = "http_traffic.log"
json_file = "traffic_data.json"

logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to process each request
def request(flow):
    """Handles HTTP(S) requests passing through mitmproxy."""
    try:
        host = flow.request.host
        url = flow.request.pretty_url
        headers = dict(flow.request.headers)
        method = flow.request.method

        log_entry = {
            "host": host,
            "url": url,
            "method": method,
            "headers": headers
        }

        # Print traffic info to console
        print(f"Captured: {method} {url}")

        # Save to log file
        logging.info(f"Request: {method} {url} - Host: {host}")

        # Save to JSON
        save_json(log_entry)

    except Exception as e:
        logging.error(f"Error processing request: {e}")

# Function to save captured data to JSON
def save_json(data):
    """Appends captured data to a JSON file."""
    try:
        with open(json_file, "a") as file:
            json.dump(data, file, indent=4)
            file.write("\n")
    except Exception as e:
        logging.error(f"Error saving to JSON: {e}")


