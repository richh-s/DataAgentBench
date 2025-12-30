code = """import json
import re

path = locals()['var_function-call-2585691326327215227']
print(f"Reading from {path}")

with open(path, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers")

titles = []
for p in papers:
    text = p.get('text', '').lower()
    # Simple check first
    if 'food' in text:
        # Regex check
        if re.search(r'\bfood\b', text):
            titles.append(p['filename'].replace('.txt', ''))

print(f"Found {len(titles)} titles")

# Prepare SQL
escaped_titles = [t.replace("'", "''") for t in titles]
titles_str = "', '".join(escaped_titles)
sql_query = f"SELECT citation_count FROM Citations WHERE title IN ('{titles_str}')"

print("__RESULT__:")
print(json.dumps(sql_query))"""

env_args = {'var_function-call-13604834933233695573': 'file_storage/function-call-13604834933233695573.json', 'var_function-call-13672825597397015902': 'file_storage/function-call-13672825597397015902.json', 'var_function-call-2585691326327215227': 'file_storage/function-call-2585691326327215227.json', 'var_function-call-4981003287102314854': [], 'var_function-call-13805358010662920095': "SELECT citation_count FROM Citations WHERE title IN ('')"}

exec(code, env_args)
