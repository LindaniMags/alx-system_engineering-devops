#!/usr/bin/python3
"""
prints a sorted count of given keyword from API
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"user-agent": "Chrome/51.0.2704.106"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    response_data = response.json()
    children = response_data["data"]["children"]

    for article in children:
        title = article["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = response_data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted:
            print(f"{word.lower()}: {count}")
