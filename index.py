from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

# Load the JSON data
with open('q-vercel-python.json', 'r') as file:
    data = json.load(file)

# Create a dictionary for quick lookup
marks_data = {entry['name']: entry['marks'] for entry in data}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        query_params = parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
        names = query_params.get('name', [])
        
        marks = [marks_data.get(name, 0) for name in names]
        
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode('utf-8'))
        return
