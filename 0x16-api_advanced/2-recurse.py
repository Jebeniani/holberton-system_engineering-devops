#!/usr/bin/python3
"""recursive function that queries the Reddit API and
returns a list containing the titles
of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API"""
    url = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla/5.0"},
                       params={"after": after})
    if url.status_code == 200:
        children = url.json().get("data").get("children")
        after = url.json().get("data").get("after")

        for element in children:
            hot_list.append(element.get("data").get("title"))

        if after is not None:
            recurse(subreddit, hot_list, after=after)
        return hot_list

    return None
