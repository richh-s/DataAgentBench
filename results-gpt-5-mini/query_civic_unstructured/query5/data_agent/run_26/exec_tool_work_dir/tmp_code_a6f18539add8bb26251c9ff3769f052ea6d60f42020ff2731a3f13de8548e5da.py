code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_qCk3641LXIXN5enTFFze5lZV, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

with open(var_call_Y9DOQHC3dDmseXvmGYGNgAg8, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_records)
# Ensure Amount is numeric
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Preprocess civic docs: lowercase texts
for d in civic_docs:
    d['text_lower'] = d['text'].lower()

# Define keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey', 'fire', 'fema/caloes', 'caljpia']
start_indicators = ['begin construction', 'advertise', 'begin:', 'begin construction:', 'begin construction -', 'begin construction -', 'begin construction', 'begin', 'start', 'start construction']

matched = []

for idx, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_low = pname.lower()
    amount = int(row['Amount'])
    found_any = False
    is_disaster = False
    started_2022 = False
    matched_docs = []
    # If project name itself contains disaster markers
    for dk in disaster_keywords:
        if dk in pname_low:
            is_disaster = True
            break
    # Search in civic docs
    for d in civic_docs:
        txt = d['text_lower']
        pos = txt.find(pname_low)
        if pos == -1:
            # Try fuzzy: remove parenthetical parts from funding project name
            pname_base = re.sub(r"\s*\(.*?\)", "", pname_low).strip()
            if pname_base and pname_base in txt:
                pos = txt.find(pname_base)
        if pos != -1:
            found_any = True
            # extract window
            start = max(0, pos-400)
            end = min(len(txt), pos+400)
            window = txt[start:end]
            # check disaster keywords in window
            for dk in disaster_keywords:
                if dk in window:
                    is_disaster = True
                    break
            # check for explicit start patterns with 2022 in document
            if '2022' in window:
                for si in start_indicators:
                    if si in window:
                        started_2022 = True
                        break
            # also check elsewhere in the whole document for patterns
            if not started_2022:
                if re.search(r'begin construction\b[^\n]{0,200}2022', txt):
                    started_2022 = True
                elif re.search(r'advertise\b[^\n]{0,200}2022', txt):
                    started_2022 = True
                elif re.search(r'begin\b[^\n]{0,200}2022', txt):
                    started_2022 = True
            matched_docs.append(d['filename'])
    matched.append({
        'Project_Name': pname,
        'Amount': amount,
        'Found_in_Docs': found_any,
        'Matched_Docs': matched_docs,
        'Is_Disaster': is_disaster,
        'Started_2022': started_2022
    })

matched_df = pd.DataFrame(matched)
# Now select rows that are disaster and started in 2022
selected = matched_df[(matched_df['Is_Disaster']==True) & (matched_df['Started_2022']==True)]

total = int(selected['Amount'].sum())

# Prepare result dict
result = {
    'total_funding_disaster_started_2022': total,
    'matched_projects_count': int(len(selected)),
    'matched_projects': selected[['Project_Name','Amount','Matched_Docs']].to_dict(orient='records')
}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_cI8eVt0Fkg4l6hxMsjm3hTmf': ['civic_docs'], 'var_call_wSFEHvsJf7lq3Z9DXUZQqQqP': ['Funding'], 'var_call_qCk3641LXIXN5enTFFze5lZV': 'file_storage/call_qCk3641LXIXN5enTFFze5lZV.json', 'var_call_Y9DOQHC3dDmseXvmGYGNgAg8': 'file_storage/call_Y9DOQHC3dDmseXvmGYGNgAg8.json'}

exec(code, env_args)
