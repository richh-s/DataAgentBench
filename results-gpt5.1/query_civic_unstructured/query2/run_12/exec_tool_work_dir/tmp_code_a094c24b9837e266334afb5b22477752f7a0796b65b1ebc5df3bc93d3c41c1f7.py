code = """import re, json
from pathlib import Path
import pandas as pd

path = Path(var_call_7kFtrZZUS6J5pp6MuYfUakgS)
civic_records = pd.read_json(path)
texts = "\n".join(civic_records['text'].tolist())

lines = [l.strip() for l in texts.split('\n') if ('Park' in l or 'park' in l)]

projects_2022 = []
for line in lines:
    if 'completed' in line.lower() and '2022' in line:
        projects_2022.append(line)

print('__RESULT__:')
print(json.dumps(projects_2022))"""

env_args = {'var_call_7kFtrZZUS6J5pp6MuYfUakgS': 'file_storage/call_7kFtrZZUS6J5pp6MuYfUakgS.json', 'var_call_j6l3rEGgWU59o73Q68ypOPJO': 'file_storage/call_j6l3rEGgWU59o73Q68ypOPJO.json'}

exec(code, env_args)
