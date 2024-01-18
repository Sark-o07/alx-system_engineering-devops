# README for 0x16.API Advanced

## Overview

This directory contains Python functions that interact with the Reddit API to retrieve information about subreddits. The provided functions cover three main functionalities: obtaining the number of subscribers for a subreddit, fetching the titles of the top ten hot posts, and recursively retrieving all hot articles for a given subreddit.

## Functions

### 1. How many subs?

#### `number_of_subscribers(subreddit)`

This function queries the Reddit API and returns the number of subscribers (total, not active users) for a given subreddit. If the provided subreddit is invalid, the function returns 0.

**Requirements:**
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- Note: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 2. Top Ten

#### `top_ten(subreddit)`

This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Requirements:**
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- Note: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 3. Recurse it!

#### `recurse(subreddit, hot_list=[])`

This recursive function queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

**Requirements:**
- Prototype: `def recurse(subreddit, hot_list=[])`
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
- If not a valid subreddit, return None.
- Note: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
- Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop, but the point is to use a recursive function. :)
