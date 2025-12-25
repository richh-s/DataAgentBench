code = """import json
import pandas as pd

# load data
path = var_call_KYjBvaLjX4G9Sl2lQN2BIqlP
with open(path, 'r') as f:
    data = json.load(f)

# create DataFrame
df = pd.DataFrame(data)

# compute description lengths
df['desc_len'] = df['description'].astype(str).str.len()

# get title of row with max description length
max_row = df.loc[df['desc_len'].idxmax()]
result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_KYjBvaLjX4G9Sl2lQN2BIqlP': 'file_storage/call_KYjBvaLjX4G9Sl2lQN2BIqlP.json'}

exec(code, env_args)
