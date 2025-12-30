code = """import json
import pandas as pd

file_path = locals()['var_function-call-11418660847891976964']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

df = pd.DataFrame(citations_data)
filenames = [t + ".txt" for t in df['title'].tolist()]

# Create the Mongo query
query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-11418660847891976964': 'file_storage/function-call-11418660847891976964.json', 'var_function-call-11418660847891976809': 'file_storage/function-call-11418660847891976809.json', 'var_function-call-17872721365629833350': {'count': 158, 'unique_titles': 158}}

exec(code, env_args)
