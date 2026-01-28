code = """# First, let's query all articles to see the data structure
query = {
    "collection": "articles",
    "filter": {},
    "projection": {"_id": 0, "article_id": 1, "title": 1, "description": 1},
    "limit": 10000  # Large enough to get all articles
}

print('__RESULT__:')
print(str(query))"""

env_args = {'var_functions.list_db:0': ['articles']}

exec(code, env_args)
