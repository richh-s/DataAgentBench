code = """import pandas as pd
import json

# Load the citation data
with open(var_call_XX9v15hK98C8XL4QVnFFFhNH, 'r') as f:
    citation_data = json.load(f)

# Check the papers found in the food domain
food_papers = []  # There are no papers in the food domain in the MongoDB

# Calculate total citation count for food domain
if food_papers:
    total_citations = sum(int(citation['total_citations']) for citation in citation_data if citation['title'] in food_papers)
else:
    total_citations = 0

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_call_XX9v15hK98C8XL4QVnFFFhNH': 'file_storage/call_XX9v15hK98C8XL4QVnFFFhNH.json', 'var_call_k3Yd1eclCRzcDmmf55VvilaF': ['paper_docs'], 'var_call_3tEUuZXbEAEwhskGsEOz8Yqs': []}

exec(code, env_args)
