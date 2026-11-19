#!/usr/bin/python3
"""Module that recursively collects the hot post titles of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/Soumaya896)"}


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if no results."""
    if hot_list is None:
        hot_list = []
    if not isinstance(subreddit, str) or not subreddit:
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=HEADERS, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return hot_list or None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list or None
    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))
    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    return hot_list or None
