from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    return f'Authorization code: {auth_code}'

if __name__ == '__main__':
    app.run(port=8888)
    # https://accounts.spotify.com/authorize?client_id=ClienID&response_type=code&redirect_uri=http://localhost:8888/callback&scope=user-read-recently-played