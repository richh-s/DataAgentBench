code = """import json
import pandas as pd

# Load data
with open(var_call_qCk3641LXIXN5enTFFze5lZV, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_Y9DOQHC3dDmseXvmGYGNgAg8, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# preprocess docs
for d in civic_docs:
    d['text_lower'] = d['text'].lower()

# keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'woolsey', 'fire']
start_indicators = ['begin construction', 'advertise', 'begin:', 'begin construction:', 'begin construction -', 'begin', 'start', 'start construction']

matched = []

for idx, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_low = pname.lower()
    amount = int(row['Amount'])
    found_any = False
    is_disaster = False
    started_2022 = False
    matched_docs = []
    # check project name for disaster markers
    for dk in disaster_keywords:
        if dk in pname_low:
            is_disaster = True
            break
    # derive base name without parenthetical suffix
    pname_base = pname_low.split('(')[0].strip()
    # search docs
    for d in civic_docs:
        txt = d['text_lower']
        # search for exact name or base
        pos = -1
        if pname_low and pname_low in txt:
            pos = txt.find(pname_low)
        elif pname_base and pname_base in txt:
            pos = txt.find(pname_base)
        if pos != -1:
            found_any = True
            # window around match
            start = max(0, pos-400)
            end = min(len(txt), pos+400)
            window = txt[start:end]
            # check disaster keywords in window
            for dk in disaster_keywords:
                if dk in window:
                    is_disaster = True
                    break
            # check for year 2022 and start indicators nearby
            if '2022' in window:
                for si in start_indicators:
                    if si in window:
                        started_2022 = True
                        break
            # as fallback, check in whole doc if any start indicator appears within 200 chars of '2022'
            if not started_2022 and '2022' in txt:
                idx2022 = txt.find('2022')
                for si in start_indicators:
                    idxsi = txt.find(si)
                    if idxsi != -1 and abs(idxsi - idx2022) < 200:
                        started_2022 = True
                        break
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
selected = matched_df[(matched_df['Is_Disaster']==True) & (matched_df['Started_2022']==True)]

total = int(selected['Amount'].sum())

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
