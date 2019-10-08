import json
from flask import Flask, render_template
import crawler
app = Flask(__name__)

@app.route('/')
def start():
    crawler.publish_report('data_file.json', crawler.find_articles(crawler.get_html_page('https://sobesednik.ru/psychology')))
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        link = data["url"]
        articles = data["articles"]
    return render_template('template.html', link=link, list=articles)
if __name__ =="__main__":
    app.run(host = '0.0.0.0', port=8000, debug=True)
