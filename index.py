import requests
from bs4 import BeautifulSoup
import json

data = {
    'male': {
        'urls': [
            'https://www.behindthename.com/submit/names/gender/masculine/usage/south-african',
            'https://www.behindthename.com/submit/names/gender/masculine/usage/south-african/2',
        ],
        'names': [],
    },
    'female': {
        'urls': [
            'https://www.behindthename.com/submit/names/gender/feminine/usage/south-african',
            'https://www.behindthename.com/submit/names/gender/feminine/usage/south-african/2',
            'https://www.behindthename.com/submit/names/gender/feminine/usage/south-african/3',
        ],
        'names': [],
    },
}


for key in data:
    for url in data[key]['urls']:
        print('now requesting from: ' + url)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        page.close()
        nameEls = soup.find_all('div', { 'class': 'browsename' })
        for nameEl in nameEls:
            name = nameEl.span.a.text
            data[key]['names'].append(name)

    file = open(key + '.json', 'w')
    file.write(json.dumps(data[key]['names']))
    file.close()