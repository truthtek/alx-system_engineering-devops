#!/usr/bin/python3

"""
queries the Reddit API and returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid subreddit is given,
return 0
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mybot"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.exceptions.HTTPError, KeyError):
        return 0
