code = """import json, re, pandas as pd
from pathlib import Path

path = Path(var_call_i33iF2i7q4p47QFcTEPlkvlN)
rows = json.loads(path.read_text())

df = pd.DataFrame(rows)

def extract_copies(text):
    m = re.search(r"(duplicated|appearing|appears|repeated|seen|copied) (\d+) times", text)
    return int(m.group(2)) if m else None

df['copies'] = df['repo_data_description'].apply(extract_copies)

df = df[df['copies'].notna()]

max_row = df.loc[df['copies'].idxmax()][['id','sample_repo_name','copies']].to_dict()

result = json.dumps(max_row)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_i33iF2i7q4p47QFcTEPlkvlN': 'file_storage/call_i33iF2i7q4p47QFcTEPlkvlN.json'}

exec(code, env_args)
