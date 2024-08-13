#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """query number of subscribers from subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    subs = data.get("subscribers")
    return subs
