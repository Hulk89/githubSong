import requests
from bs4 import BeautifulSoup
import numpy as np
from flask import render_template, Flask


url = "https://github.com/"

def makeData(userName):
    '''
    make data from github profile url
    '''
    res = requests.get(url + userName)
    soup = BeautifulSoup(res.text, 'lxml')
    svg = soup.find('svg', attrs={'class': 'js-calendar-graph-svg'})

    cols = svg.find('g').findAll('g')

    data = np.zeros((7, len(cols)), np.uint8)
    for i, col in enumerate(cols):
        rects = col.findAll('rect')
        for j, rect in enumerate(rects):
            if int(rect['data-count']) != 0:
                data[j][i] = 1
    data = data.flatten()
    commit_list = data.tolist()
    return commit_list

app = Flask(__name__)

@app.route('/<username>')
def hello(username):
    return render_template('index.html', github_data=makeData(username))

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)