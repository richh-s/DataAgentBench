code = """import json
import os

# Load articles data
articles = locals()['var_functions.query_db:2']
if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

# Find sports articles using keywords
sports_keywords = ['sports', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 
'golf', 'olympics', 'athlete', 'game']

max_length = 0
title_with_max_length = ""

for article in articles:
    title = article.get('title', '').lower()
    desc = article.get('description', '')
    
    is_sports = any(keyword in title or keyword in desc.lower() for keyword in sports_keywords)
    
    if is_sports and len(desc) > max_length:
        max_length = len(desc)
        title_with_max_length = article.get('title', '')

# Print result in required format
print("__RESULT__:")
print(json.dumps(title_with_max_length))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
