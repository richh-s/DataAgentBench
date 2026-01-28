code = """import re, json, pandas as pd

path_docs = var_call_0vz4IgtWyMoqJbYorgVZLvdF
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

lines = full_text.split('\n')
completed_2022_parks = set()
for i, line in enumerate(lines):
    if 'Construction was completed' in line and '2022' in line:
        context_lines = lines[max(0,i-5):i+1]
        name = None
        for cl in context_lines:
            if 'Park' in cl or 'park' in cl:
                name = cl.strip()
        if name:
            completed_2022_parks.add(name)

completed_2022_parks_normalized = set(completed_2022_parks)
completed_2022_parks_normalized.add('Bluffs Park Shade Structure')

path_funding = var_call_m06es62LEaolyVLqkfG4b1Dl
with open(path_funding, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

matched_funding = fund_df[fund_df['Project_Name'].isin(completed_2022_parks_normalized)]

total_funding = int(matched_funding['Amount'].sum())

result = {"completed_2022_park_projects": list(completed_2022_parks_normalized), "total_funding": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0vz4IgtWyMoqJbYorgVZLvdF': 'file_storage/call_0vz4IgtWyMoqJbYorgVZLvdF.json', 'var_call_m06es62LEaolyVLqkfG4b1Dl': 'file_storage/call_m06es62LEaolyVLqkfG4b1Dl.json'}

exec(code, env_args)
