# HTTPSBackdoor

## Overview

A Backdoor program which acts as a simple Command and Control (C2) server as well as client, transmitting and receiving data through encrypted covert channels of the SSL and TLS over the HTTP protocol.

The program uses HTTP Cookies as its heart, through which it transmits Base64 encoded commands and receives its output.

## Usage

- Create Self-Signed Certificates using OpenSSL

```bash
mkdir auth
openssl req -new -x509 -newkey rsa:4096 -nodes -keyout auth/key.pem -out auth/cert.pem -days 10000
```

- Run the HTTPS Server
```bash
python3 https.py 2>/dev/null
```

- Run the client on the victim side
```bash
python3 client.py
```

## Note

The server and client listening and connecting addresses are hardcoded in the source files. In order to make most of these programs, please consider to change them according to your desired needs.

## Disclaimer
This project is intended for educational and security testing purposes only. The author is not responsible for any misuse of this tool.

## Author
Developed by **Sayan Ray** [@BareBones90](https://x.com/BareBones90)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
