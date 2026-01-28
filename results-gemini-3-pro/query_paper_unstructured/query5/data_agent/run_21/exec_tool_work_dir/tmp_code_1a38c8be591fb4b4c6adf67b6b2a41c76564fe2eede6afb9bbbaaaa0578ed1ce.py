code = """import json
import sqlite3
import re

# Load the citation results
with open(locals()['var_function-call-12669116658095172213'], 'r') as f:
    citations_data = json.load(f)

# Extract titles and map title -> citation_count
title_to_citations = {item['title']: item['citation_count'] for item in citations_data}
titles = list(title_to_citations.keys())

print(f"Total papers cited in 2020: {len(titles)}")
print(f"First 5 titles: {titles[:5]}")

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-8178165909663735325': ['Citations', 'sqlite_sequence'], 'var_function-call-8178165909663733532': ['paper_docs'], 'var_function-call-12669116658095172213': 'file_storage/function-call-12669116658095172213.json', 'var_function-call-5093665862301701388': 'file_storage/function-call-5093665862301701388.json'}

exec(code, env_args)
