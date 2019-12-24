# Fetch content from medium.com


# This test server fetches the specified url from medium.com
# with proper user credntials and starts a server at localhost:5000
# where it serves the acquired article.

from flask import Flask
import requests
import time


# Change the cookie data to your own.
cookie_data = [
    {
        "key": "uid",
        "value": "564f5af43366",
        "domain": ".medium.com",
        "path": "/",
        "expires": str(time.mktime((2020, 12, 20, 6, 48, 10, 0, 0, 0)))
    },
    {
        "key": "sid",
        "value": "1:qVh3VQ8dlwIlmWW3NILqHh8a/E4xwKgTK1kPp5l8MG56IlmdzMyfuLXLapFudrhn",
        "domain": ".medium.com",
        "path": "/",
        "expires": str(time.mktime((2020, 12, 20, 6, 48, 10, 0, 0, 0)))
    }
]

jar = requests.cookies.RequestsCookieJar()

for cookie in cookie_data:
    jar.set(cookie["key"], cookie["value"], domain=cookie["domain"],
            path=cookie["path"], expires=cookie["expires"], secure=True)

resp = requests.get(
    "https://medium.com/hackernoon/learn-functional-python-in-10-minutes-to-2d1651dece6f", cookies=jar)

f = open("temp.html", "w")
f.write(resp.text)
f.close()

app = Flask(__name__)


@app.route("/")
def hello():
    f = open("temp.html", "r")
    data = f.read()
    f.close()
    return data


if __name__ == "__main__":
    app.run()
