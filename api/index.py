from http.server import BaseHTTPRequestHandler
from bot import main
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        os.environ['TELEGRAM_TOKEN'] = 'VOTRE_TOKEN_BOT'  # À remplacer
        main()
        self.wfile.write('Bot Telegram démarré'.encode())
