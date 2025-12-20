code = """import json

with open('var_function-call-11639742510862021534', 'r') as f:
    data = json.load(f)

print(f"Total articles: {len(data)}")
article_ids = [item['article_id'] for item in data]
# Print first 5 to check format
print(f"First 5 IDs: {article_ids[:5]}")
# Print the list of ids as a JSON string so I can use it in the next step, 
# but only if it's not massive. If it's massive, I might need another strategy.
# Let's check the length first.
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-11639742510862021534': 'file_storage/function-call-11639742510862021534.json'}

exec(code, env_args)
