code = """import re, json
from pathlib import Path

path = Path(var_call_kojKLy0chRj9lhHKhhWTt8x3)
with open(path, 'r') as f:
    civic_docs = json.load(f)

project_lines = []
for doc in civic_docs:
    text = doc.get('text','')
    for line in text.split('\n'):
        if '2022' in line:
            project_lines.append(line.strip())

path2 = Path(var_call_sgc8Rsb9bDTP2glUKHPWar28)
with open(path2, 'r') as f:
    funding = json.load(f)

# determine disaster-related projects by funding name patterns
patterns = ['(fema project)', '(fema/caloes project)', '(caloes project)', '(caljpia project)', '(fema)', '(caljpia/fema project)']

total_disaster_amount = 0
for row in funding:
    name = row['Project_Name']
    low = name.lower()
    if any(p in low for p in patterns):
        try:
            amt = int(row['Amount'])
        except Exception:
            try:
                amt = float(row['Amount'])
            except Exception:
                amt = 0
        total_disaster_amount += amt

result = json.dumps(total_disaster_amount)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_kojKLy0chRj9lhHKhhWTt8x3': 'file_storage/call_kojKLy0chRj9lhHKhhWTt8x3.json', 'var_call_sgc8Rsb9bDTP2glUKHPWar28': 'file_storage/call_sgc8Rsb9bDTP2glUKHPWar28.json'}

exec(code, env_args)
