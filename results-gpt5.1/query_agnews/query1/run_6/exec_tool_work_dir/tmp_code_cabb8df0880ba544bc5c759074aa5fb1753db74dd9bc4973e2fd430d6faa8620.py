code = """import json
import pandas as pd

path = var_call_7QFNYUuoG4kVRdvsUZLDfoeg
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['desc_len'] = df['description'].astype(str).str.len()
max_row = df.sort_values('desc_len', ascending=False).iloc[0]
result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7QFNYUuoG4kVRdvsUZLDfoeg': 'file_storage/call_7QFNYUuoG4kVRdvsUZLDfoeg.json'}

exec(code, env_args)
