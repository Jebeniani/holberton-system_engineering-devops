#!/usr/bin/python3
"""Number of subs"""
import requests


def number_of_subscribers(subreddit):
    """
    Number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url.format(subreddit), headers=headers)
    try:
        subscribers = r.json().get("data").get("subscribers")
        return subscribers
    except Exception:
        return 0
