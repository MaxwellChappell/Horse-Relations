import requests
from bs4 import BeautifulSoup
import numpy as np

relation_values = {
    "1" : 0.5,
    "2" : 0.25,
    "3" : 0.125,
    "4" : 0.0625,
    "5" : 0.03125,
}

def sort_dict(d):
    keys = list(d.keys())
    values = list(d.values())
    sort = np.argsort(values)
    sorted_d = {keys[i]: values[i] for i in sort[::-1]}
    return sorted_d

def relation(horse):
    relative = {}

    url = f"https://www.pedigreequery.com{horse}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("td", class_=["f", "m"])

    for line in results:
        if line.find("a"):
            name = line.find("a").attrs.get("href")
            gen = line.attrs.get("data-g")
            if name in relative:
                relative[name] += relation_values[gen]
            else:
                relative[name] = relation_values[gen]
    return relative


