code = """import json
import sqlite3

# Load the citations result
citations_path = locals()['var_function-call-16918491452103176986']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Extract titles and create a map for citation counts
title_to_citations = {}
for c in citations:
    title_to_citations[c['title']] = c['citation_count']

print(f"Total papers cited in 2018: {len(title_to_citations)}")
print(f"Sample titles: {list(title_to_citations.keys())[:5]}")

# Prepare filenames for MongoDB query
filenames = [t + ".txt" for t in title_to_citations.keys()]

print("__RESULT__:")
print(json.dumps({"count": len(filenames), "filenames_sample": filenames[:5]}))"""

env_args = {'var_function-call-16918491452103176986': 'file_storage/function-call-16918491452103176986.json', 'var_function-call-2065725143731253530': 'file_storage/function-call-2065725143731253530.json'}

exec(code, env_args)
