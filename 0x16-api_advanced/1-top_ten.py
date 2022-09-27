#!/usr/bin/python3
"""Gather data from an API"""
import requests


def top_ten(subreddit):
    """the top ten hot posts"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        subs = r.json().get('data').get('children')
        for subscriber in range(10):
            print(subs[subscriber].get('data').get('title'))
    else:
        print("None")
