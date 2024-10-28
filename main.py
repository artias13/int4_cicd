import os
from flask import Flask, request, jsonify, Response
from dotenv import load_dotenv

load_dotenv()
HOST_URL = os.getenv('HOST_URL')

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        
    def setup_routes(self):
        @self.app.route('/', methods=['GET', 'OPTIONS'])
        def home():
            return Response("404 Try /healthz bro", status=404) 

        @self.app.route('/healthz', methods=['GET', 'OPTIONS'])
        def healthz():
            return Response("200 OK", status=200)

    def run(self, debug, port, host):
        print(f'ну давай, нападай: http://{host}:{port}')
        self.app.run(debug=debug, port=port, host=host)

if __name__ == '__main__':
    server = Server()
    server.run(debug=True, port=8225, host=str(HOST_URL))
