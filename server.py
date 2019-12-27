# Fetch content from medium.com


# This test server fetches the specified url from medium.com
# with proper user credntials and starts a server at localhost:5000
# where it serves the acquired article.

# Server extended to support any article from medium.com, towardsdatascience.com etc.
# Example query : https://localhost:5000/medium.com/{path_to_article}

# Disables medium's scripts and injects custom scripts

from flask import Flask
import requests
from process import PageProcessor
from cookies import load_cookies
import logging


# ------- CONFIGURATIONS ---------
LITE_MODE = True       # Set only for fast testing puposes
LOG_TO_FILE = True


# Create a .env file with the relevant cookie information
cookie_data = load_cookies()


# Logging
if LOG_TO_FILE:
    logging.basicConfig(filename="server.log", level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
else:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


# Add custom cookies to request
jar = requests.cookies.RequestsCookieJar()

for cookie in cookie_data:
    jar.set(cookie["key"], cookie["value"], domain=cookie["domain"],
            path=cookie["path"], expires=cookie["expires"], secure=True)


app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello(path):
    url = "https://" + path
    resp = requests.get(url, cookies=jar)
    if resp.status_code == 200:
        app.logger.info('%s retrieved successfully' % url)
        processor = PageProcessor(resp.text)
        return processor.process_page() if not LITE_MODE else processor.process_page_lite()
    else:
        app.logger.info('Error %d retrieving %s' % (resp.status_code, url))
        return "404: Page not found"


if __name__ == "__main__":
    app.run()
