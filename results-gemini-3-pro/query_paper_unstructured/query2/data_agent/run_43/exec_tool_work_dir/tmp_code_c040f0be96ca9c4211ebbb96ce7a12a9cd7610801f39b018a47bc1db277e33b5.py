code = """import json
import pandas as pd

file_path = locals()['var_function-call-11418660847891976964']
with open(file_path, 'r') as f:
    citations_data = json.load(f)

df = pd.DataFrame(citations_data)
filenames = [t + ".txt" for t in df['title'].tolist()]

# Batch 1: first 80
batch1 = filenames[:80]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": batch1}
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-11418660847891976964': 'file_storage/function-call-11418660847891976964.json', 'var_function-call-11418660847891976809': 'file_storage/function-call-11418660847891976809.json', 'var_function-call-17872721365629833350': {'count': 158, 'unique_titles': 158}, 'var_function-call-14199248049921182924': 'file_storage/function-call-14199248049921182924.json'}

exec(code, env_args)
