# Fetch content from medium.com


# This test server fetches the specified url from medium.com
# with proper user credntials and starts a server at localhost:5000
# where it serves the acquired article.

# Server extended to support any article from medium.com, towardsdatascience.com etc.
# Example query : https://localhost:5000/medium.com/{path_to_article}

# Renders everything in an iframe with scripts disabled
# Loads images well but messes up any iframes within the article and links

from flask import Flask, render_template
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

# Add custom cookies to request
jar = requests.cookies.RequestsCookieJar()

for cookie in cookie_data:
    jar.set(cookie["key"], cookie["value"], domain=cookie["domain"],
            path=cookie["path"], expires=cookie["expires"], secure=True)


# save the response
# f = open("temp.html", "w")
# f.write(resp.text)
# f.close()

app = Flask(__name__)

#
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    url = "https://" + path
    resp = requests.get(url, cookies=jar)
    if resp.status_code == 200:
        return render_template('iframes.html', article=resp.text)
    else:
        return "404: Page not found"


if __name__ == "__main__":
    app.run()
