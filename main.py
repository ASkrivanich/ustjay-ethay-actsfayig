import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def do_post(text_to_post):
    # headers = {
    #     "Host": "hidden-journey-62459.herokuapp.com",
    #     "Connection": "keep-alive",
    #     "Cache-Control": "max-age=0",
    #     "Origin": "http://hidden-journey-62459.herokuapp.com",
    #     "Upgrade-Insecure-Requests": "1",
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Referer": "http://hidden-journey-62459.herokuapp.com/"
    # }
    response = requests.post("http://hidden-journey-62459.herokuapp.com/piglatinize/",
                             data={'input_text': text_to_post}, allow_redirects=False)#, headers = header)
    print(response.headers)
    return response.text


@app.route('/')
def home():
    fact = get_fact()
    return do_post(fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)
