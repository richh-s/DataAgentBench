code = """import json
import pandas as pd

with open(locals()['var_function-call-3447372631833955035'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
paper_titles = df_citations['title'].tolist()

query_filter = {"filename": {"$in": [title + ".txt" for title in paper_titles]}}
query_projection = {"text": 1, "filename": 1}

print("__RESULT__:")
print(json.dumps({"filter": query_filter, "projection": query_projection}))"""

env_args = {'var_function-call-3447372631833955035': 'file_storage/function-call-3447372631833955035.json'}

exec(code, env_args)
