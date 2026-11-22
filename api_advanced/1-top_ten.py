#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/Soumaya896)"}


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=HEADERS, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        print(None)
        return
    for child in data.get("children", []):
        print(child.get("data", {}).get("title"))
