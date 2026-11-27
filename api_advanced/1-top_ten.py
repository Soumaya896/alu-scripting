#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Query Reddit API and print first 10 hot post titles or None."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/soumaya896)"}
    params = {"limit": 10}

    try:
        resp = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10,
        )
        if resp.status_code != 200:
            print(None)
            return

        children = resp.json().get("data", {}).get("children", [])
        if not children:
            print(None)
            return

        for item in children[:10]:
            title = item.get("data", {}).get("title")
            if title is not None:
                print(title)
    except Exception:
        print(None)
