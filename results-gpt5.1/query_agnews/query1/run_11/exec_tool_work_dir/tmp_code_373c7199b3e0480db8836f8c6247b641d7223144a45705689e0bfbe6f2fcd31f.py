code = """import json
import pandas as pd

path = var_call_kzs02cCBSBDyqDR5q8kwlguG
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# compute length of description
df['desc_len'] = df['description'].astype(str).str.len()
max_row = df.loc[df['desc_len'].idxmax()]
result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kzs02cCBSBDyqDR5q8kwlguG': 'file_storage/call_kzs02cCBSBDyqDR5q8kwlguG.json'}

exec(code, env_args)
