from flask import flask
import threading
import requests
import time

app = Flask(__name__)

urls = [
    'https://rowingstatsflask.onrender.com',
    'https://listedbuildings.onrender.com'
]
#intervals in seconds (840s=14mins)
interval = 840

def keepAlive():
    while True:
        for url in urls:
            try:
                response = requests.get(url)
                print(f'Pinged {url}: {response.status_code}')
            except Exception as e:
                print(f'Error pinging {url}: {e}')
        time.sleep(interval)

threading.Thread(target=keepAlive, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)