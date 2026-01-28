code = """import json
import pandas as pd

# Load citation data from storage
path = var_call_OPW69TUMfhI829BPa4syYqbX
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure numeric
df['citation_count'] = pd.to_numeric(df['citation_count'])
avg = df['citation_count'].mean()

res = json.dumps(avg)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_OPW69TUMfhI829BPa4syYqbX': 'file_storage/call_OPW69TUMfhI829BPa4syYqbX.json'}

exec(code, env_args)
