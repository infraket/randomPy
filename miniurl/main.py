import random
import string

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
shortened_urls = {}

counter = 0
counter_short = {}


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()

        shortened_urls[short_url] = long_url
        return f"Shortened url: {request.url_root}{short_url}<br> <br>GO TO THE STATS {request.url_root}stats/{short_url}"

    return render_template("index.html", counter=counter)


@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)

    global counter
    if long_url:
        counter += 1
        counter_short[short_url] = counter_short.get(short_url, 0) + 1
        return redirect(long_url)
    else:
        "URL not found", 404


@app.route("/stats/<short_url>")
def get_stats(short_url):
    try:

        return f"STATS url: TOTAL: {counter} <br><br> STATS ON SHORT_URL - {short_url} : {counter_short[short_url]}"


    except:

        return f"URL not found OR no one has crossed it yet, GO TO The short URL"


if __name__ == "__main__":
    app.run(debug=True)
