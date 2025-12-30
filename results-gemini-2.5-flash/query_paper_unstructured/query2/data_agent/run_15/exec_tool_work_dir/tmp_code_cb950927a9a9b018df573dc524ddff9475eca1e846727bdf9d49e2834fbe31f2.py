code = """import json
import pandas as pd

with open(locals()['var_function-call-10318410833687957099'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
titles = df_citations['title'].tolist()

# Prepare MongoDB query for paper_docs collection to get filename and text
# The filenames in paper_docs_database match the titles in citations_database
# without the .txt extension. So, we need to add .txt to the titles.
mongo_filter_titles = [title + ".txt" for title in titles]

mongo_query = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": mongo_filter_titles}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-10318410833687957099': 'file_storage/function-call-10318410833687957099.json'}

exec(code, env_args)
