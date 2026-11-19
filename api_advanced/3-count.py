#!/usr/bin/python3
"""Module that counts keywords in the hot post titles of a subreddit."""
import requests

HEADERS = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/Soumaya896)"}


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively print sorted keyword counts for hot post titles.

    Prints nothing if the subreddit is invalid or no keyword matches.
    """
    if not isinstance(subreddit, str) or not subreddit or not word_list:
        return
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100}
    if after:
        params["after"] = after
    data = None
    try:
        response = requests.get(url, headers=HEADERS, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code == 200:
            data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        data = None
    if data is not None:
        for child in data.get("children", []):
            title = child.get("data", {}).get("title") or ""
            for token in title.lower().split():
                counts[token] = counts.get(token, 0) + 1
        if data.get("after"):
            return count_words(subreddit, word_list, data.get("after"),
                               counts)
    totals = {}
    for word in word_list:
        word = word.lower()
        if counts.get(word):
            totals[word] = totals.get(word, 0) + counts[word]
    ordered = sorted(totals.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, total in ordered:
        print("{}: {}".format(word, total))
