code = """import json
import pandas as pd

path = var_call_CYhFoiuHCRtvtq5tYszP6KRa
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['desc_len'] = df['description'].astype(str).str.len()
max_row = df.loc[df['desc_len'].idxmax()]
result = max_row['title']

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_CYhFoiuHCRtvtq5tYszP6KRa': 'file_storage/call_CYhFoiuHCRtvtq5tYszP6KRa.json'}

exec(code, env_args)
