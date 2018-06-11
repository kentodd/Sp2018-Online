#!/usr/bin/env python
"""
Starting point for lesson9 assignment - Ken Murray
"""

import time
import requests

WORD = "trump"

NEWS_API_KEY = "3660a22fe4704ee3bc3226fc6ac63421"

base_url = 'https://newsapi.org/v2/'


def get_sources():
    """Get news sources"""
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("here are all of the sources")
    print(sources)
    return sources


def get_articles(source):
    """get the articles from the sources"""
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top",
              }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print("Something Very Bad Has Happened with {)".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return titles


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


start = time.time()
sources = get_sources()

art_count = 0
word_count = 0
for source in sources:
    titles = get_articles(source)
    art_count += len(titles)
    word_count += count_word('trump', titles)

print(WORD, "found {} times in {} articles".format(word_count, art_count))
print("process took {:.0f} seconds".format(time.time() - start))





