#!/usr/bin/python3
"""Module that queries the Reddit API for the top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alx.api.advanced:v1.0 (by /u/alx)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    children = response.json().get("data", {}).get("children", [])
    for post in children[:10]:
        print(post.get("data", {}).get("title"))
