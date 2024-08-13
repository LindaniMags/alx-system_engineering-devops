#!/usr/bin/python3
"""
parses the title of all hot articles,
and prints a sorted count of given keyword
"""
import requests


def count_words(subreddit, word_list, num={}, after="", count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Chrome/51.0.2704.106"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        response_json = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    response_json = response_json.get("data")
    after = response_json.get("after")
    count += response_json.get("dist")
    for val in response_json.get("children"):
        title = val.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                occur = len([t for t in title if t == word.lower()])
                if num.get(word) is None:
                    num[word] = occur
                else:
                    num[word] += occur

    if after is None:
        if len(num) == 0:
            print("")
            return
        num = sorted(num.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in num]
    else:
        count_words(subreddit, word_list, num, after, count)
