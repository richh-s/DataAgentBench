code = """import json
import os

# Load the SQLite result
with open('var_function-call-974393757557094033.json', 'r') as f:
    citations_data = json.load(f)

# Extract titles and create a map of title -> citation_count
title_citation_map = {item['title']: item['citation_count'] for item in citations_data}
titles = list(title_citation_map.keys())
filenames = [t + ".txt" for t in titles]

print(f"Number of papers cited in 2018: {len(filenames)}")
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-974393757557094033': 'file_storage/function-call-974393757557094033.json'}

exec(code, env_args)
