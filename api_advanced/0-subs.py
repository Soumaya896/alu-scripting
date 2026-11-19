#!/usr/bin/python3
"""Module that gets the number of subscribers of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/Soumaya896)"}


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, headers=HEADERS,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        data = response.json().get("data", {})
        return data.get("subscribers", 0) or 0
    except (requests.RequestException, ValueError):
        return 0
