#!/usr/bin/python3
"""Module that prints the first 10 hot post titles of a subreddit."""
import requests

HEADERS = {
    "User-Agent": "python:alu.api_advanced.top_ten:v1.0 (by /u/Soumaya896)"
}


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params={"limit": 10},
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children")
    except (requests.RequestException, ValueError):
        print(None)
        return
    if not posts:
        print(None)
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
