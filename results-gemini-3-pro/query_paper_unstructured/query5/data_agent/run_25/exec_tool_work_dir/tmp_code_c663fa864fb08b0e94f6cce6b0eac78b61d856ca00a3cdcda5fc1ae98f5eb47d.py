code = """import json
import re

# Load citations
with open('var_function-call-3704779829923578766.json', 'r') as f:
    citations = json.load(f)

# Extract titles and map title to citation count
title_to_citations = {}
for c in citations:
    title = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    title_to_citations[title] = count

titles = list(title_to_citations.keys())
filenames = [t + ".txt" for t in titles]

print(f"Total papers cited in 2020: {len(titles)}")
print(f"First 5 filenames: {filenames[:5]}")

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-3704779829923578766': 'file_storage/function-call-3704779829923578766.json', 'var_function-call-4076760790261236942': 'file_storage/function-call-4076760790261236942.json'}

exec(code, env_args)
