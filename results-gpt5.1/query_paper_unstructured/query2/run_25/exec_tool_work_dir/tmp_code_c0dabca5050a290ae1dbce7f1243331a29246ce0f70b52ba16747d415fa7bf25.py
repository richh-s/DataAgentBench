code = """import json
import pandas as pd
from pathlib import Path

file_path = var_call_XCE7CBWdgDqsKKCfPZdNpjDD
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['citation_count'] = pd.to_numeric(df['citation_count'])
avg = df['citation_count'].mean()

res = json.dumps(avg)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_XCE7CBWdgDqsKKCfPZdNpjDD': 'file_storage/call_XCE7CBWdgDqsKKCfPZdNpjDD.json'}

exec(code, env_args)
