#!/usr/bin/python3
"""Module that prints the first 10 hot post titles of a subreddit."""
import requests

USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "python:alu.api_advanced.top_ten:v1.0 (by /u/Soumaya896)",
]


def _fetch_hot_json(subreddit):
    """Fetch JSON payload for /r/<subreddit>/hot.json without redirects."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    for ua in USER_AGENTS:
        headers = {
            "User-Agent": ua,
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            response = requests.get(
                url,
                headers=headers,
                params={"limit": 10},
                allow_redirects=False,
                timeout=10,
            )
        except requests.RequestException:
            continue

        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return None
        if response.status_code in (301, 302, 303, 307, 308, 404):
            return None
    return None


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return

    payload = _fetch_hot_json(subreddit)
    if not isinstance(payload, dict):
        print(None)
        return

    posts = payload.get("data", {}).get("children")
    if not posts:
        print(None)
        return

    for post in posts[:10]:
        if isinstance(post, dict):
            title = post.get("data", {}).get("title")
            if title is not None:
                print(title)
