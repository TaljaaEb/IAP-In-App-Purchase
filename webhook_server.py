# Eben Taljaard
# webhook_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
from datetime import datetime

received_webhooks = []


class WebhookHandler(BaseHTTPRequestHandler):

    def _send(self, status=200, content_type="text/plain"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path

        # Existing line-item endpoint
        if path == "/lineitems":
            self._send(200, "text/plain")

            for ln in lineitems:
                self.wfile.write(
                    f"<custom>{ln}</custom>\n".encode()
                )

            return

        # Webhook inspection endpoint
        if path == "/webhooks":
            self._send(200, "application/json")

            response = json.dumps(
                received_webhooks,
                indent=2
            )

            self.wfile.write(response.encode())
            return

        self._send(404)
        self.wfile.write(b"Not Found")

    def do_POST(self):
        self.receive_webhook()

    def do_PUT(self):
        self.receive_webhook()

    def do_PATCH(self):
        self.receive_webhook()

    def do_DELETE(self):
        self.receive_webhook()

    def receive_webhook(self):

        parsed = urlparse(self.path)

        # Read request body
        content_length = int(
            self.headers.get("Content-Length", 0)
        )

        body = self.rfile.read(content_length)

        try:
            body_text = body.decode("utf-8")
        except UnicodeDecodeError:
            body_text = repr(body)

        # Capture headers
        headers = {
            key: value
            for key, value in self.headers.items()
        }

        webhook = {
            "time": datetime.now().isoformat(),
            "method": self.command,
            "path": parsed.path,
            "query": parsed.query,
            "client": self.client_address[0],
            "headers": headers,
            "body": body_text,
        }

        received_webhooks.append(webhook)

        # Console inspection
        print("\n" + "=" * 70)
        print("WEBHOOK RECEIVED")
        print("=" * 70)
        print(f"Time   : {webhook['time']}")
        print(f"Method : {self.command}")
        print(f"Path   : {parsed.path}")
        print(f"Client : {self.client_address[0]}")

        print("\nHeaders:")
        for key, value in headers.items():
            print(f"  {key}: {value}")

        print("\nBody:")
        print(body_text)
        print("=" * 70)

        # Webhook.site-like response
        self._send(200, "application/json")

        response = {
            "ok": True,
            "received": True,
            "method": self.command,
            "path": parsed.path,
        }

        self.wfile.write(
            json.dumps(response).encode()
        )

    def log_message(self, format, *args):
        # Prevent BaseHTTPRequestHandler's normal duplicate logging
        pass
####
    # inside WebhookHandler

    def do_POST(self):

        if self.path == "/webhook/iap":
            self.receive_iap_webhook()
            return
    
        self.receive_webhook()
    
    
    def receive_iap_webhook(self):
    
        content_length = int(
            self.headers.get(
                "Content-Length",
                0
            )
        )
    
        body = self.rfile.read(
            content_length
        )
    
        try:
            payload = json.loads(
                body.decode("utf-8")
            )
        except Exception:
    
            self.send_response(400)
            self.end_headers()
    
            self.wfile.write(
                b"Invalid JSON"
            )
    
            return
    
        print()
        print("=" * 60)
        print("IAP WEBHOOK")
        print("=" * 60)
    
        print(json.dumps(
            payload,
            indent=2
        ))
    
        # Forward into application logic
        from callback import process_callback
    
        result = process_callback(payload)
    
        self.send_response(200)
    
        self.send_header(
            "Content-Type",
            "application/json"
        )
    
        self.end_headers()
    
        self.wfile.write(
            json.dumps(result).encode()
        )
###

# --------------------------------------------------
# Existing line items
# --------------------------------------------------

lineitems = [
    "I0010|Widget|2|R100.00",
    "I0020|Service|1|R250.00",
]


def run_http_server(host="0.0.0.0", port=5555):

    server_address = (host, port)

    httpd = HTTPServer(
        server_address,
        WebhookHandler
    )

    print()
    print("Webhook collector started")
    print("----------------------------------------")
    print(f"Webhook URL : http://localhost:{port}/webhook")
    print(f"Line items  : http://localhost:{port}/lineitems")
    print(f"Inspector   : http://localhost:{port}/webhooks")
    print("----------------------------------------")
    print("Waiting for webhooks...")
    print()

    httpd.serve_forever()


if __name__ == "__main__":
    run_http_server()
