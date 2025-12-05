code = """import json
import pandas as pd
import tempfile

file_path = var_call_GFXpUJRNOGYEDzG0uezcqkAV
with open(file_path, 'r') as f:
    data = json.load(f)

repo_names = [row['repo_name'].replace("'", "''") for row in data]

df = pd.DataFrame({'repo_name': repo_names})

tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')

df.to_csv(tmp_file.name, index=False)

result = json.dumps({'csv_path': tmp_file.name})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_8GNAqHg9hq08TxOBQKuXEW5m': [{'cnt': '15016'}], 'var_call_GFXpUJRNOGYEDzG0uezcqkAV': 'file_storage/call_GFXpUJRNOGYEDzG0uezcqkAV.json'}

exec(code, env_args)
