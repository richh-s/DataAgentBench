code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_lUc8U0BZqMAL1bI1wh408X1
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d['text'] for d in civic_docs)

# Heuristic: find project lines mentioning parks/playgrounds and completion dates in 2022
project_patterns = [
    r'Trancas Canyon Park Playground',
    r'Trancas Canyon Park Upper and Lower Slopes Repair',
    r'Malibu Bluffs Park South Walkway Repairs?',
    r'Malibu Bluffs Park Roof Replacement Project',
    r'Bluffs Park Shade Structure',
    r'Legacy Park [^\n]*',
]

completed_2022_projects = set()
for pat in project_patterns:
    for m in re.finditer(pat, texts):
        name = m.group(0).strip()
        window = texts[m.end():m.end()+300]
        if re.search(r'completed[^\d]*2022', window, re.IGNORECASE) or re.search(r'Construction was completed,?\s*November 2022', window):
            completed_2022_projects.add(name)

# Manually add from visible preview where clear
# From preview: "Bluffs Park Shade Structure" completed November 2022
completed_2022_projects.add('Bluffs Park Shade Structure')

# Load funding table
path_fund = var_call_Enq79d6pbhESJXBYVNMAJ3Zw
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Normalize for matching: simple exact name match using known park-related names
park_keywords = ['Park', 'Playground']
park_fund = fund_df[fund_df['Project_Name'].str.contains('|'.join(park_keywords), case=False, na=False)].copy()

# Limit to those completed in 2022 based on our detected names
if completed_2022_projects:
    park_fund_2022 = park_fund[park_fund['Project_Name'].isin(list(completed_2022_projects))]
else:
    park_fund_2022 = park_fund.iloc[0:0]

total_funding = int(park_fund_2022['Amount'].sum())

result = {
    'completed_2022_projects': sorted(list(completed_2022_projects)),
    'matching_funding_records': park_fund_2022.to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lUc8U0BZqMAL1bI1wh408X1J': 'file_storage/call_lUc8U0BZqMAL1bI1wh408X1J.json', 'var_call_Enq79d6pbhESJXBYVNMAJ3Zw': 'file_storage/call_Enq79d6pbhESJXBYVNMAJ3Zw.json'}

exec(code, env_args)
