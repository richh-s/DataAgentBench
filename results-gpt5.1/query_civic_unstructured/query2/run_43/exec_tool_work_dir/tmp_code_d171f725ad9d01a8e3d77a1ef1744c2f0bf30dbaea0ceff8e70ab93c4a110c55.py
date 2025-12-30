code = """import json
from pathlib import Path

# load full funding from file path
path_funding = Path(var_call_rCr9nxSjnQepYJN90r0RiutX)
with open(path_funding, 'r') as f:
    funding = json.load(f)

project_names_2022 = ['Bluffs Park Shade Structure']

total = 0
for row in funding:
    if row['Project_Name'] in project_names_2022:
        total += int(row['Amount'])

result = json.dumps({"total_funding_2022_park_completed": total})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_gui95wiHvIiRKwUzXLKmymGG': 'file_storage/call_gui95wiHvIiRKwUzXLKmymGG.json', 'var_call_rCr9nxSjnQepYJN90r0RiutX': 'file_storage/call_rCr9nxSjnQepYJN90r0RiutX.json', 'var_call_hgFk8h9IDoCj2lFYa2GfsQVU': ['Bluffs Park Shade Structure']}

exec(code, env_args)
