code = """import json
import re

# Load citation data
with open(locals()['var_function-call-7183846072918696098'], 'r') as f:
    citation_data = json.load(f)

# Extract paper titles from citation data and prepare them for MongoDB query
paper_titles = [item['title'] for item in citation_data]
filenames = [f'{title}.txt' for title in paper_titles]

# Construct MongoDB query for all filenames
mongo_query = {"collection": "paper_docs", "filter": {"filename": {"$in": filenames}}, "projection": {"filename": 1, "text": 1}}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-7183846072918696098': 'file_storage/function-call-7183846072918696098.json', 'var_function-call-4716046700129101370': 'file_storage/function-call-4716046700129101370.json', 'var_function-call-4665120397400476245': 'file_storage/function-call-4665120397400476245.json', 'var_function-call-16008961785518209763': 'file_storage/function-call-16008961785518209763.json', 'var_function-call-5521543360950345533': 'file_storage/function-call-5521543360950345533.json'}

exec(code, env_args)
