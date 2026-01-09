code = """import json, pandas as pd
from pathlib import Path

# load symbol list
p = Path(var_call_TWmoaj5nxzkNWCttpzyMj9Oo)
records = json.loads(p.read_text())
df = pd.DataFrame(records)
# keep simple company name before ' is '
df['name'] = df['company_name'].str.split(' is part of | is a | is an | specializes in | operates | offers | provides | excels |,', n=1, regex=True).str[0].str.strip()
symbols = df['Symbol'].tolist()

# emit list for next step (batched querying outside python not possible here)
print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'name_map': dict(zip(df['Symbol'], df['name']))}))"""

env_args = {'var_call_TWmoaj5nxzkNWCttpzyMj9Oo': 'file_storage/call_TWmoaj5nxzkNWCttpzyMj9Oo.json'}

exec(code, env_args)
