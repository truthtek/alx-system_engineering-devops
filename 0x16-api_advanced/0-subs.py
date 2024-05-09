#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    resp_data = res.json()
    if 'data' not in resp_data:
        return 0

    data = resp_data['data']
    if 'subscribers' not in data:
        return 0

    subscribers = data['subscribers']
    if subscribers > 0:
        return "OK"
    else:
        return 0
