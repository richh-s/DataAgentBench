code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

civic = load_records(var_call_3kP2iva4O3n0zEGnBKj333Yh)
fund = load_records(var_call_RrHO73RThtmh1QERe5SjORe7)

# Build funding map
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Parse projects with schedule lines from civic docs
text_all = "\n".join(doc.get('text','') for doc in civic)

# Find blocks: Project name line followed by 'Project Schedule' section containing 'Begin Construction:'
pattern = re.compile(r"\n(?P<name>[^\n]{3,120})\n\n\(cid:190\) Updates:.*?\(cid:190\) Project Schedule:.*?\(cid:131\) Begin Construction:\s*(?P<begin>[^\n]+)", re.S)

matches = list(pattern.finditer(text_all))
rows = []
for m in matches:
    name = m.group('name').strip()
    begin = m.group('begin').strip()
    rows.append({'Project_Name': name, 'begin': begin})

# Also capture 'Estimated Schedule' blocks
pattern2 = re.compile(r"\n(?P<name>[^\n]{3,120})\n\n\(cid:190\) Updates:.*?\(cid:190\) Estimated Schedule:.*?\(cid:131\) Begin Construction:\s*(?P<begin>[^\n]+)", re.S)
for m in pattern2.finditer(text_all):
    name = m.group('name').strip()
    begin = m.group('begin').strip()
    rows.append({'Project_Name': name, 'begin': begin})

# Deduplicate by name with earliest begin string
df = pd.DataFrame(rows).drop_duplicates(subset=['Project_Name','begin'])

# Define Spring 2022 match
spring_2022 = df[df['begin'].str.contains(r"\bSpring\s+2022\b", case=False, na=False)]

# Join funding
spring_2022['funding'] = spring_2022['Project_Name'].map(fund_map).fillna(0).astype(int)

count = int(spring_2022['Project_Name'].nunique())
total_funding = int(spring_2022.drop_duplicates('Project_Name')['funding'].sum())

out = {'projects_started_spring_2022_count': count, 'total_funding_usd': total_funding, 'projects': spring_2022.drop_duplicates('Project_Name')[['Project_Name','funding']].sort_values('Project_Name').to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xQBuDOOz4TwqooSFSZrF5pqX': ['Funding'], 'var_call_WWDRnFbR27qZDng5NwQOLFRr': ['civic_docs'], 'var_call_3kP2iva4O3n0zEGnBKj333Yh': 'file_storage/call_3kP2iva4O3n0zEGnBKj333Yh.json', 'var_call_RrHO73RThtmh1QERe5SjORe7': 'file_storage/call_RrHO73RThtmh1QERe5SjORe7.json'}

exec(code, env_args)
