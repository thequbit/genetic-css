import sys

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
import json

import urllib2
from bs4 import BeautifulSoup

#import css
from analyse_css import analyse_url

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyse", methods=['POST'])
def analyse():
    url = request.form['url']

    #flash("analysing '{0}'".format(url))

    res = analyse_url(url)

    #jsondata = json.dumps(res)

    #print >> sys.stderr, jsondata

    return "file can be compressed: {0} characters.".format(
        res.cost)

    #return "hello."

    #return url

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0')
