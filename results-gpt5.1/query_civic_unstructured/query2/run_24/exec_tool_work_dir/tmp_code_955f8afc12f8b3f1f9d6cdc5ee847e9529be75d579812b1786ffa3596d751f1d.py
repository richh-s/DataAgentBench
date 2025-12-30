code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_MhnWy3lFLYeyqycXKHyp6Re4)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
funding = pd.DataFrame(var_call_Adk46D1h9D5e3Dteq3wOdAVb)
funding['Amount'] = funding['Amount'].astype(int)

# Very rough heuristic: treat any project name containing 'Park' or 'Playground' as park-related
park_funding = funding[funding['Project_Name'].str.contains('Park|Playground', case=False, regex=True)]

# We need only those park projects that were completed in 2022.
# Try to detect completion year from civic docs text by matching "<project name>" and nearby "completed" with a 2022 date.
texts = ' \n '.join(d['text'] for d in civic_docs)

completed_2022_projects = set()
for name in park_funding['Project_Name'].unique():
    # Escape regex special chars in name
    pattern = re.escape(name)
    # search windows around the project name
    for m in re.finditer(pattern, texts, flags=re.IGNORECASE):
        start = max(0, m.start()-300)
        end = m.end()+300
        window = texts[start:end]
        if re.search(r'completed[^\n]*2022', window, flags=re.IGNORECASE) or re.search(r'2022[^\n]*completed', window, flags=re.IGNORECASE):
            completed_2022_projects.add(name)
            break

filtered = park_funding[park_funding['Project_Name'].isin(completed_2022_projects)]

total_funding = int(filtered['Amount'].sum())

result = {"total_funding_completed_2022_park_projects": total_funding,
          "projects": filtered[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MhnWy3lFLYeyqycXKHyp6Re4': 'file_storage/call_MhnWy3lFLYeyqycXKHyp6Re4.json', 'var_call_Adk46D1h9D5e3Dteq3wOdAVb': 'file_storage/call_Adk46D1h9D5e3Dteq3wOdAVb.json'}

exec(code, env_args)
