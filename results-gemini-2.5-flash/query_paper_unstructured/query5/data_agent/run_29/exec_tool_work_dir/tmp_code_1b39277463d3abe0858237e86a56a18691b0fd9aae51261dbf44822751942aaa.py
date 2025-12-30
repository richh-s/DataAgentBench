code = """import json
import pandas as pd

with open(locals()['var_function-call-12458711442629031814'], 'r') as f:
    citation_titles = json.load(f)

# Prepare filter for MongoDB query
filters = []
for title in citation_titles:
    filters.append({"filename": f"{title}.txt"})

mongo_query = {"collection": "paper_docs", "filter": {"$or": filters}, "projection": {"filename": 1, "text": 1}}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-9866274534013825103': 'file_storage/function-call-9866274534013825103.json', 'var_function-call-12458711442629031814': 'file_storage/function-call-12458711442629031814.json'}

exec(code, env_args)
