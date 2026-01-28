code = """import json
import os

# Load articles from storage
articles_key = 'var_functions.query_db:2'
articles_data = locals()[articles_key]

# If it's a file path, read the file
if isinstance(articles_data, str) and os.path.exists(articles_data):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    # Direct data
    articles = articles_data

print("Total articles loaded:", len(articles))

# Calculate description lengths
for article in articles:
    article['desc_length'] = len(article.get('description', ''))

# Sort by description length
top_articles = sorted(articles, key=lambda x: x['desc_length'], reverse=True)[:10]

print("Top 10 longest descriptions:")
for i, article in enumerate(top_articles, 1):
    print(f"{i}. Length: {article['desc_length']} - Title: {article.get('title', 'N/A')}")
    print(f"   Desc start: {article.get('description', 'N/A')[:80]}...")
    print()"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
