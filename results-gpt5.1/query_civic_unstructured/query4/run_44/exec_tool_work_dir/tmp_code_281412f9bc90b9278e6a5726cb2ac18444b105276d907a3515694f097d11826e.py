code = """import re, json, pandas as pd
from pathlib import Path

path_civic = Path(var_call_cjQ01fgHbBGIc5YrBtwgFRqy)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

path_fund = Path(var_call_vcVmxcshSaazOSuem1b9stgX)
with open(path_fund, 'r') as f:
    funding = json.load(f)

text_all = "\n".join(d['text'] for d in civic_docs)
lines = [l.strip() for l in text_all.split('\n') if l.strip()]

projects = []
current = None
pattern = re.compile(r'^[A-Z0-9].*(Project|Improvements|Repairs|Resurfacing|Drainage|Canyon Park Playground|Water Treatment Facility)')

for line in lines:
    if pattern.match(line):
        current = {'Project_Name': line, 'st': None}
        projects.append(current)
    elif current and 'Begin Construction:' in line:
        current['st'] = line.split('Begin Construction:')[-1].strip()
    elif current and 'Advertise:' in line and current['st'] is None:
        current['st'] = line.split('Advertise:')[-1].strip()

spring_keywords = ['Spring 2022', '2022-Spring']
projects_spring_2022 = {p['Project_Name'] for p in projects if p['st'] and any(k in p['st'] for k in spring_keywords)}

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask = fund_df['Project_Name'].isin(projects_spring_2022)
sel = fund_df[mask]

result = {
    'projects_started_spring_2022_count': int(mask.sum()),
    'total_funding_spring_2022': int(sel['Amount'].sum()),
    'matched_projects': sel[['Project_Name', 'Amount']].to_dict(orient='records')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_cjQ01fgHbBGIc5YrBtwgFRqy': 'file_storage/call_cjQ01fgHbBGIc5YrBtwgFRqy.json', 'var_call_vcVmxcshSaazOSuem1b9stgX': 'file_storage/call_vcVmxcshSaazOSuem1b9stgX.json'}

exec(code, env_args)
