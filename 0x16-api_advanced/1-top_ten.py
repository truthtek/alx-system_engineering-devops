#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If the subreddit is invalid, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:reddit-api-project:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("None")
            return

        for post in posts:
            title = post["data"]["title"]
            print(title)

    except (requests.exceptions.HTTPError, KeyError):
        print("None")
