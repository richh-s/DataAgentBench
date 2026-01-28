code = """import json
import pandas as pd
from pathlib import Path

path = var_call_Wbpje8ptKuD0Lx42Th54cuou
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# extract titles from filenames
df['title'] = df['filename'].str.replace('.txt', '', regex=False)

result = df['title'].drop_duplicates().to_list()
result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_Wbpje8ptKuD0Lx42Th54cuou': 'file_storage/call_Wbpje8ptKuD0Lx42Th54cuou.json'}

exec(code, env_args)
