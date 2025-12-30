code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-15672313218616885663'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)

titles = citations_df['title'].tolist()
filenames = [t + ".txt" for t in titles]

# Construct MongoDB query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "limit": 1000  # Should be enough for 158 papers
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-15672313218616885663': 'file_storage/function-call-15672313218616885663.json', 'var_function-call-15672313218616887976': 'file_storage/function-call-15672313218616887976.json', 'var_function-call-11255294213250427348': 'file_storage/function-call-11255294213250427348.json', 'var_function-call-3978247635877250414': {'citations_count': 158, 'papers_count': 5}}

exec(code, env_args)
