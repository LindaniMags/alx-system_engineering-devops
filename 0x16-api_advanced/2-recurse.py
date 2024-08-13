#!/usr/bin/python3
"""uses recursion to query API for all titles of hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    if after is None:
        return []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?"
    url += f"limit=100&after={after}"
    headers = {"User-Agent": "Chrome/51.0.2704.106"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    response_json = response.json()
    hot_articles = response.json.get('data').get('children')
    for article in hot_articles:
        hot_list.append(article.get("data").get("title"))
    after = response_json.get("data").get("after")
    return hot_articles + recurse(subreddit, [], after)
