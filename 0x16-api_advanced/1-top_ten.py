#!/usr/bin/python3
"""Gather data from an API"""
import requests


def top_ten(subreddit):
    """the top ten hot posts"""
    url = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla/5.0"},
                       params={"limit": "10"})
    if url.status_code == 200:
        for element in url.json().get('data').get('children'):
            if element.get('data').get('title'):
                print(element.get('data').get('title'))
    else:
        print("None")
