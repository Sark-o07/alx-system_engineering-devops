#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or  not isinstance(subreddit, str):
        return 0

    headers = {'user-agent': 'Google Chrome Version 120.0.6099.234'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=headers, allow_redirects=False)
    

    print("response: {}".format(response))
    if response.status_code != 200:
        return 0
    try:
        results = response.json()
        return results.get('data').get('subscribers')
    except Exception:
        return 0
