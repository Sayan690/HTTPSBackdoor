#!/usr/bin/env python3

import os

if __name__ == '__main__':
	if "auth" not in os.listdir():
		os.mkdir("auth")
		os.system("openssl req -new -x509 -newkey rsa:4096 -nodes -keyout auth/key.pem -out auth/cert.pem -days 10000")

	else:
		if "cert.pem" not in os.listdir("auth/") and "key.pem" not in os.listdir("auth/"):
			os.system("openssl req -new -x509 -newkey rsa:4096 -nodes -keyout auth/key.pem -out auth/cert.pem -days 10000")

	os.system("python3 -m pip install -r requirements.txt")