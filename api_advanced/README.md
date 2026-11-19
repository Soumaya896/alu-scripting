# API Advanced

Python scripts that query the Reddit API with the Requests module.

| File | What it does |
|------|--------------|
| 0-subs.py | `number_of_subscribers(subreddit)` returns the total subscribers, 0 if the subreddit is invalid |
| 1-top_ten.py | `top_ten(subreddit)` prints the titles of the first 10 hot posts, None if invalid |
| 2-recurse.py | `recurse(subreddit, hot_list=None, after=None)` recursively returns all hot post titles, None if invalid |
| 3-count.py | `count_words(subreddit, word_list)` recursively counts keywords in hot titles and prints them sorted |

All scripts set a custom User-Agent and do not follow redirects.

Author: Soumaya896
