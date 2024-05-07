import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:reddit-api-project:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.exceptions.HTTPError, KeyError):
        return 0
