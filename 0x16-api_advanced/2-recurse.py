
#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of titles of all hot posts for a given subreddit.
    If no results are found for the given subreddit, the function returns None.

    Args:
        subreddit (str): The subreddit to search for hot posts.
        hot_list (list, optional): The list to store hot post titles.
        after (str, optional): The `after` parameter for the Reddit API.

    Returns:
        list or None: A list of hot post titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:reddit-api-project:v1.0 (by /u/your_username)"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            return hot_list

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after)

    except (requests.exceptions.HTTPError, KeyError):
        return None
