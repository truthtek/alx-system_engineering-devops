#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return -1.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        data = req.json().get("data")
        if data:
            return data.get("subscribers", 0)
        else:
            return -1  # Subreddit does not exist
    else:
        return -1  # Request failed

# Example usage:
subreddit_name = "example_subreddit"
subscribers = number_of_subscribers(subreddit_name)
if subscribers == -1:
    print(f"The subreddit '{subreddit_name}' does not exist or could not be accessed.")
else:
    print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")

