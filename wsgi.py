import json
from flask import Flask, render_template, request, redirect, url_for
import crawler

app = Flask(__name__)


@app.route('/')
def start():
    crawler.publish_report('data_file.json',
                           crawler.find_articles(crawler.get_html_page('https://sobesednik.ru/psychology')))
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        link = data["url"]
        articles = data["articles"]
    return render_template('template.html', link=link, list=articles)


@app.route('/process_data/', methods=['POST'])
def doit():
    return redirect(url_for("start"))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
